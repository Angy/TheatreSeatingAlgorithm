from app.models import User, Section, Seat


def allocate_seats():
    """
    first class seating arrangement; has no section/seat type restriction
    second class seating arrangement; has access to seats in the first balcony
    third class seating arrangement; has access to seats in the second balcony
    """

    rank_one_user = [user for user in User.objects.all() if user.rank == "one"]
    rank_two_user = [user for user in User.objects.all() if user.rank == "two"]
    rank_three_user = [user for user in User.objects.all() if user.rank == "three"]

    grouped_user = [rank_one_user, rank_two_user, rank_three_user]
    sorted_group = sorted(grouped_user, key=len)

    for user_group in sorted_group:
        if user_group:
            _get_allocated_seats(user_group)


def _adjacent_seat_occupied(seat):
    #todo : check that the adjacent seat is occupied
    pass


def _get_section(user_group):
    if user_group[0].rank == 'one':
        accesible_sections = Section.objects.all()
    elif user_group[0].rank == 'two':
        accesible_sections = Section.objects.filter(section_name__in=['first_balcony'])
    else:
        accesible_sections = Section.objects.filter(section_name__in=['second_balcony'])

    return list(accesible_sections)


def _get_seats(sections):
    seat_data = [section.rows.all().values('seats') for section in sections]

    if seat_data:
        seats = list(seat_data[0])
        available_seats = Seat.objects.filter(
            row_seat__in=[seat['seats'] for seat in seats], is_blocked=False
        )
        return available_seats
    return None


def _get_allocated_seats(user_with_rank):
    allocated_seats = []

    section = _get_section(user_with_rank)
    available_seats = _get_seats(section)
    if available_seats:
        for user in user_with_rank:

            # check if the user has a seat preference:
            preference = user.has_preference
            for seat in available_seats:

                if preference:
                    allocated_seat = Seat.objects.get(
                        seat_number=preference.seat_number
                    )
                else:
                    allocated_seat = Seat.objects.get(seat_number=seat.seat_number)

                allocated_seat.allocated_to = user
                allocated_seat.is_blocked = True
                allocated_seat.save()
                allocated_seats.append(allocated_seat)
                break

    return allocated_seats
