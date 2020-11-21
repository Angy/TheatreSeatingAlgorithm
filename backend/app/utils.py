from app.models import User, Seat, Row, Section, Hall


def create_user(user_fixture=None):
    users = []
    if user_fixture:
        users.append(User.objects.create(**user_fixture))
    else:
        for i in range(1, 3):
            users.append(User.objects.create(rank='one'))
            users.append(User.objects.create(rank='two'))
            users.append(User.objects.create(rank='three'))
    return users


def create_seat(seat_fixture):
    user, _ = User.objects.get_or_create(id=seat_fixture.pop('allocated_to'))
    seat = Seat.objects.create(**seat_fixture, allocated_to=user)
    return seat

def create_row(row_fixture):
    seats = row_fixture.pop('seats')

    row = Row.objects.create(**row_fixture)
    for seat in seats:
        new_seat = create_seat(seat)
        row.seats.add(new_seat)
    return row.save()


def create_section(section_fixture):
    rows = section_fixture.pop('rows')

    section = Section.objects.create(**section_fixture)
    for row in rows:
        new_seat = create_row(row)
        section.rows.add(new_seat)
    return section.save()


def create_hall(hall_fixture):
    sections = hall_fixture.pop('sections')

    hall = Hall.objects.create(**hall_fixture)
    for row in sections:
        new_seat = create_row(row)
        hall.sections.add(new_seat)
    return hall.save()

