from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import User, Seat, Row, Section, Hall


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'rank', )


class SeatSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Seat
        exclude = ('id', )


class RowSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True)

    class Meta:
        model = Row
        exclude = ('id', )

    def create(self, data):
        seats = data.pop('seats')
        row, _ = Row.objects.get_or_create(row_number=data['row_number'])
        if row.seats.count() > 20 or len(seats) > 20:
            raise ValidationError('A row can have only 20 seats')
        else:
            for seat in seats:
                seat_data, _ = Seat.objects.get_or_create(**seat)
                row.seats.add(seat_data)

        return row


class SectionSerializer(serializers.ModelSerializer):
    rows = RowSerializer(many=True)

    class Meta:
        model = Section
        exclude = ('id', )

    def create(self, data):
        rows = data.pop('rows')
        section_name = data['section_name']
        section, _ = Section.objects.get_or_create(
            section_name=section_name.capitalize()
        )
        if section.rows.count() > 10 or len(rows) > 10:
            raise ValidationError('A section can have only 10 rows')
        else:
            for row in rows:
                row_data, _ = Row.objects.get_or_create(**row)
                section.rows.add(row_data)

        return section


class HallSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Hall
        exclude = ('id', )

    def create(self, data):
        sections = data.pop('sections')
        hall_name = data.pop('name')

        hall, _ = Hall.objects.get_or_create(name=hall_name.capitalize())
        for section in sections:
            section_data, _ = Section.objects.get_or_create(**section)
            hall.sections.add(section)
        return hall
