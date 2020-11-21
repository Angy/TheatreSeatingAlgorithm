# Theatre Seating Arrangement

## Overview

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

#### Running the seating algorithm

```
cd backend
docker exec -it <web_container_id>' bash (can be found using *docker ps*)
python manage.py shell
from app.tasks import *
allocate_seats()
```


#### APIs
* api/v1/halls/ 
* api/v1/rows/
* api/v1/rows/<row_number>
* api/v1/seats/
* api/v1/users/
* api/v1/users/<user_rank>

See `urls.py` for more details


## Frontend Implementation

#### Run
`cd frontend`

`npm start`

##### To start the build

`cd frontend`

`npm run build`


## Improvements (Yet to be implemented):
* Allow adding multiple sections
* Limit no. of rows per section
* Limit no. of seats per row
* Restrict no. of aisle seats based on the alignment of rows/sections
* Restrict Front row seat based on the alignment of rows
* Auto create aisle seats for a row (only 2 in a row)
* Auto generate assure adjacent seats are occupied
* Unique Section & Hall names
* Raise error incase of insufficient no. of seats
