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
    seats = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = Row
        exclude = ('id', )


class SectionSerializer(serializers.ModelSerializer):
    rows = RowSerializer(many=True)

    class Meta:
        model = Section
        exclude = ('id', )

    def create(self, data):
        rows = data.pop('rows')
        section, _ = Section.objects.get_or_create(section_name=data['section_name'])
        print('>>>>>>>>>>>', _)
        print(section.rows.count())
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

