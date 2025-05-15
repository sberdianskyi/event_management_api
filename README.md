
# Event Management API

REST API service for managing events and user registrations.

## Installation using GitHub

1. Clone the repository:

```shell
git clone https://github.com/sberdianskyi/event_management_api.git
```

2. Create and activate virtual environment:

```shell
python -m venv venv
venv\Scripts\activate # for Windows
source vevn/bin/activate # for MacOS/Linux
```
3. Install requirements:

```shell
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Don't forget to fill your .env file according to .env_example

## Run with Docker

Docker should be installed and you need to be in directory with docker-compose.yml file

```shell
docker-compose build
docker-compose up
```

## Getting access

Register a new user using the `/api/user/register/` endpoint.
Obtain an authentication(access) token by sending a POST request 
to the `/api/user/login/` endpoint with your username and password. 
Use the obtained token in the authorization header(`Authorization: Token <Your access token>`) for accessing 
protected endpoints.

## API Endpoints

### User Management

* POST /api/user/register/ - Create new user

* POST /api/user/login/ - Get auth token

### Events

* GET /api/event_management/events/ - List events

* POST /api/event_management/events/ - Create event

* GET /api/event_management/events/{id}/ - Get event details

* PUT/PATCH /api/event_management/events/{id}/ - Update event

* DELETE /api/event_management/events/{id}/ - Delete event

### Event Registrations
* GET /api/event_management/registrations/ - List registrations

* POST /api/event_management/registrations/ - Register for event

* DELETE /api/event_management/registrations/{id}/ - Cancel registration
