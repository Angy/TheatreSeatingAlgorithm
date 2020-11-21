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
    "id": 10,
    "seat_number": 10,
    "seat_type": "aisle",
    "allocated_to": 1
}
seat_fixture1 = {
    "id": 11,
    "seat_number": 11,
    "seat_type": "balcony",
    "allocated_to": 2
}
seat_fixture2 = {
    "id": 12,
    "seat_number":12,
    "seat_type": "balcony",
    "allocated_to": None
}

seat_fixture3 = {
    "id": 13,
    "seat_number": 13,
    "seat_type": "aisle",
    "allocated_to": None
}

row_fixture = {
    "row_number": 6,
    "seats": [seat_fixture, seat_fixture1, seat_fixture2, seat_fixture3]
}

section_fixture = {
    "section_name": "first_balcony",
    "rows": [row_fixture]
}
