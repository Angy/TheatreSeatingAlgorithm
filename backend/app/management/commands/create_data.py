from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from app.models import Seat, Row, Section, Hall
from app.utils import create_user, create_seat


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = create_user()
        rows = []
        seats = []

        hall = Hall.objects.create()

        sections = Section.objects.bulk_create([
            Section(section_name=Section.MAIN_HALL),
            Section(section_name=Section.FIRST_BALCONY),
            Section(section_name=Section.SECOND_BALCONY)
             ])

        for i in range(1, 3):
            row = Row.objects.create(row_number=i)
            rows.append(row)

        for i in range(1, 5):
            seat =Seat.objects.create(seat_number=i, seat_type='aisle')

            for row in rows:
                row.seats.add(seat)

                for section in Section.objects.all():
                    section.rows.add(row)
                    hall.sections.add(section)

        self.stdout.write('Command executed successfully !')

