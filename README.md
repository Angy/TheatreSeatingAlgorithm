# Theatre Seating Arrangement

## overview

The seating arrangement algorithm is implemented to categorise the users based
 on their ranks and allocate seats accordingly. The project is split into
  Backend(uses Django) and Frontend (uses REACT)
 
 The key implementations are as follows:
 
* User can rank first class, second class or third class
* First class users are not restricted to the sections or seats
* Second class users can be allocated seats from the first balcony or the second
 balcony
* Second class users can be allocated seats from second balcony
* A seat can only be reserved for one user at a time and is blocked once reserved
* Seating arrangement is based on the user groups (i.e. user ranks)
* Users can set their seat preference. If the preference is set, the set is
 blocked
* Only users with access to a seat in within the section can opt for the
  preference of that seat.
* Adjacent seats are assigned to the users
  

## Backend Implementation
#### Run
`cd backend`

`docker-compose up --build`

#### Tests
`cd backend`

`docker-compose run web bash -c 'python manage.py test'`

#### Creating a superuser
`cd backend`

`docker-compose run web bash -c 'python manage.py create_superuser'`

#### Creating dummy dataset
`cd backend`

`docker-compose run web bash -c 'python manage.py create_data'`


#### APIs
* api/v1/halls/ 
* api/v1/rows/
* api/v1/rows/<row_number>
* api/v1/seats/
* api/v1/users/
* api/v1/users/<user_id>

See `urls.py` for more details


## Frontend Implementation

####Run
`cd backend`

`npm start`

