from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from app.models import Seat, Row, Section, Hall
from app.utils import create_user, create_seat


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = create_user()
        rows = []
        seats = []

        for i in range(1, 10):
            seats.append(Seat.objects.create(seat_number=i, seat_type='aisle'))

        for i in range(1, 3):
            row = Row.objects.create(row_number=i)
            row.seats.add(seats)
            rows.append(row)

        sections = Section.objects.bulk_create(
            [Section(section_name=Section.MAIN_HALL)],
            [Section(section_name=Section.FIRST_BALCONY)],
            [Section(section_name=Section.SECOND_BALCONY)],
        )
        for section in sections:
            section.rows.add(rows)

        hall = Hall.objects.create()
        hall.sections.add(sections)

        self.stdout.write('Command executed successfully !')

