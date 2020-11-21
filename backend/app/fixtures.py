user_fixture = {
    "id": 1,
    "user_name": "Test User",
    "rank": "one"
}
user_fixture1 = {
    "id": 2,
    "user_name": "Test User",
    "rank": "one"
}
user_fixture2 = {
    "id": 3,
    "user_name": "Test User",
    "rank": "one"
}
user_fixture3 = {
    "id": 4,
    "user_name": "Test User",
    "rank": "two"
}

seat_fixture = {
    "id": 1,
    "seat_number": 1,
    "seat_type": "aisle",
    "allocated_to": 1
}
seat_fixture1 = {
    "id": 2,
    "seat_number": 2,
    "seat_type": "aisle",
    "allocated_to": 2
}
seat_fixture2 = {
    "id": 4,
    "seat_number": 4,
    "seat_type": "aisle",
    "allocated_to": 3
}

seat_fixture3 = {
    "id": 3,
    "seat_number": 3,
    "seat_type": "aisle",
    "allocated_to": 4
}

row_fixture = {
    "row_number": 6,
    "row_seat": [seat_fixture, seat_fixture1, seat_fixture2, seat_fixture3]
}

section_fixture = {
    "section_name": "first_balcony",
    "rows": [row_fixture]
}