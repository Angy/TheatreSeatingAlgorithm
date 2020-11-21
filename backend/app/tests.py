import copy

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from app.fixtures import row_fixture, seat_fixture
from app.models import Seat, User, Row


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_seat(self):
        user = User.objects.create(id=seat_fixture['allocated_to'])
        seat_data = copy.deepcopy(seat_fixture)
        seat_data['allocated_to'] = user.id

        url = reverse('seats')
        response = self.client.post(url, data=seat_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Seat.objects.count(), 1)

    def test_post_row(self):
        row_data = copy.deepcopy(row_fixture)

        url = reverse('rows')
        response = self.client.post(url, data=row_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Row.objects.count(), 1)
