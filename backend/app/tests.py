import copy

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from app.fixtures import row_fixture, seat_fixture, section_fixture
from app.models import Seat, User, Row, Section
from app.tasks import allocate_seats
from app.utils import create_seat, create_user


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_seat(self):
        user = User.objects.create(rank='one')
        seat_data = copy.deepcopy(seat_fixture)
        seat_data['allocated_to'] = user.id

        url = reverse('seats')
        response = self.client.post(url, data=seat_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Seat.objects.count(), 1)

    def test_post_row_without_seats(self):
        row_data = copy.deepcopy(row_fixture)

        url = reverse('rows')
        response = self.client.post(url, data=row_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Row.objects.count(), 1)

    def test_post_row_with_seats(self):
        row_data = copy.deepcopy(row_fixture)

        seats = []

        for i in range(1, 9):
            seat = Seat.objects.create(id=i, seat_number=i, seat_type='balcony')
            seats.append(seat)

        row_data['seats'] = seats
        url = reverse('rows')
        response = self.client.post(url, data=row_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Row.objects.count(), 1)


class TestTasks(TestCase):

    def test_seat_allocation(self):
        test_row = row_fixture
        test_section = section_fixture
        seat_fixture = test_row.pop('seats')

        row = Row.objects.create(**test_row)

        # create few extra seats:
        for i in range(1, 9):
            extra_seat = Seat.objects.create(id=i,
                                             seat_number=i,
                                             seat_type='balcony')
            row.seats.add(extra_seat)

        for seat in seat_fixture:
            seat_obj = create_seat(seat)
            row.seats.add(seat_obj)

        test_section.pop('rows')
        section = Section.objects.create(**test_section)
        section.rows.add(row)

        all_users = create_user()

        allocate_seats()

        users_without_seats = User.objects.filter(seat__is_blocked=False)
        self.assertEqual(Seat.objects.all().count(), 12)
        self.assertEqual(Seat.objects.filter(is_blocked=True).count(), 4)
