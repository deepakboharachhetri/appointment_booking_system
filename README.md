# Salon System API

A small Django REST API for managing salon services and appointments. Staff members can sign in with JWT authentication, manage the services offered by the salon, and create or update appointments.

## What it includes

- JWT login and token refresh
- Service management with name, price, and duration
- Appointment management with customer details, service selection, date, time, status, and notes
- Search and filtering for appointments
- Validation to prevent past appointments and duplicate time slots
- SQLite database for local development

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/) (recommended)

## Getting started

From the project directory:

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

The superuser must be a staff user because the service and appointment endpoints require staff permissions.

## Authentication

Get an access token with a username and password:

```http
POST /api/token/
Content-Type: application/json
```

```json
{
	"username": "your-username",
	"password": "your-password"
}
```

Use the returned access token on protected requests:

```http
Authorization: Bearer <access-token>
```

When the access token expires, request a new one:

```http
POST /api/token/refresh/
Content-Type: application/json
```

```json
{
	"refresh": "<refresh-token>"
}
```

## API endpoints

### Services

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | `/api/services/` | List services |
| POST | `/api/services/` | Create a service |
| GET | `/api/services/<id>/` | View one service |
| PUT | `/api/services/<id>/` | Replace a service |
| DELETE | `/api/services/<id>/` | Delete a service |

Example service:

```json
{
	"name": "Haircut",
	"price": "25.00",
	"duration": 30
}
```

`price` cannot be negative, `duration` must be greater than zero, and the service name cannot be blank.

### Appointments

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | `/api/appointments/` | List appointments |
| POST | `/api/appointments/` | Create an appointment |
| GET | `/api/appointments/<id>/` | View one appointment |
| PATCH | `/api/appointments/<id>/` | Update an appointment |
| DELETE | `/api/appointments/<id>/` | Delete an appointment |
| PATCH | `/api/appointments/<id>/update-status/` | Change only the status |

Example appointment:

```json
{
	"customer_name": "Jordan Lee",
	"customer_phone": "555-123-4567",
	"service": 1,
	"status": "pending",
	"appointment_date": "2026-09-20",
	"appointment_time": "14:30:00",
	"notes": "First visit"
}
```

The `service` value is the ID of an existing service. Valid statuses are `pending`, `confirmed`, `completed`, and `cancelled`.

Appointments cannot be scheduled in the past, and each date/time combination can only be booked once. Phone numbers may contain spaces, hyphens, and parentheses, but must contain 7 to 15 digits.

Appointments can be filtered by status or date:

```text
/api/appointments/?status=confirmed
/api/appointments/?appointment_date=2026-09-20
```

They can also be searched by customer name or phone number:

```text
/api/appointments/?search=Jordan
```

## Admin site

The Django admin is available at:

```text
http://127.0.0.1:8000/admin/
```

Sign in with the superuser created during setup.

## Running checks

```bash
uv run python manage.py check
uv run python manage.py test
```

## Project layout

```text
accounts/       Authentication-related models and permissions
appointments/   Appointment model, API, validation, and routes
services/       Service model, API, validation, and routes
config/         Django settings and URL configuration
manage.py       Django management entry point
db.sqlite3      Local development database
```
