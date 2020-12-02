from django.db import models


class User(models.Model):
    ONE = 'one'
    TWO = 'two'
    THREE = 'three'

    RANK = ((ONE, 'one'), (TWO, 'two'), (THREE, 'three'),)

    user_name = models.CharField(max_length=120)
    rank = models.CharField(max_length=10, choices=RANK)
    seat_preference = models.ForeignKey('Seat', on_delete=models.CASCADE,
                                        blank=True, null=True)

    def __str__(self):
        return self.user_name

    @property
    def has_preference(self):
        if self.seat_preference:
            return True
        return False


class Seat(models.Model):
    AISLE = 'aisle'
    FRONT_ROW = 'front_row'
    BALCONY = 'balcony'
    SEATS = ((AISLE, 'Aisle'),
             (FRONT_ROW, 'Front Row'),
             (BALCONY, 'Balcony'),
             )
    seat_number = models.PositiveIntegerField(default=1, unique=True)
    seat_type = models.CharField(max_length=20, choices=SEATS)
    allocated_to = models.ForeignKey(User, on_delete=models.CASCADE,
                                     blank=True, null=True)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return f'{str(self.seat_number)} : {self.seat_type}'

    def clean(self):
        if self.allocated_to:
            self.is_blocked = True

    @property
    def is_aisle(self):
        if self.seat_type == 'aisle':
            return True
        return False


class Row(models.Model):
    row_number = models.PositiveIntegerField()
    seats = models.ManyToManyField(Seat, related_name='row_seat', blank=True)

    def __str__(self):
        return str(self.row_number)


class Section(models.Model):
    section_name = models.CharField(max_length=25,
                                    unique=True,
                                    default='Main hall')
    rows = models.ManyToManyField(Row, related_name='section_row')

    def __str__(self):
        return self.section_name


class Hall(models.Model):
    name = models.CharField(max_length=25, default='Zaal 1')
    sections = models.ManyToManyField(Section, related_name='hall_section')

    def __str__(self):
        return self.name

