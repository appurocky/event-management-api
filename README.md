#  Event Management API

A simple Django REST Framework-based API for managing events and attendees.

---

## Features

* Create and list events
* Register attendees for specific events
* View attendees of a specific event
* Auto-generated API docs with Swagger and ReDoc

---

##  Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/appurocky/event-management-api.git
   cd event-management-api
   ```

2. **Install Dependencies**

   ```bash
   pip install django
   pip install djangorestframework
   pip install drf-yasg
   ```

3. **Run Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

5. **Access the API Documentation**

   * Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
   * ReDoc UI: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

##  API Endpoints

| Method | Endpoint                                     | Description                         |
| ------ | -------------------------------------------- | ----------------------------------- |
| POST   | `/api/events`                                | Create an event                     |
| GET    | `/api/events/`                               | List upcoming events                |
| POST   | `/api/events/<event_id>/register`            | Register an attendee for an event   |
| GET    | `/api/events/<event_id>/attendees`           | List attendees for a specific event |
| PUT    | `/api/attendees/<attendee_id>/update-email/` | Update attendee's email             |

---

📡 Sample API Calls (Plain Format)
✅ Create Event
Method: POST

URL: http://127.0.0.1:8000/api/events

Headers:

Content-Type: application/json

Body:

json
Copy
Edit
{
  "name": "Tech Conference",
  "start_time": "2025-07-01T18:00:00Z",
  "end_time": "2025-07-01T21:00:00Z",
  "max_attendees": 100
}
✅ Register Attendee
Method: POST

URL: http://127.0.0.1:8000/api/events/1/register

Headers:

Content-Type: application/json

Body:

json
Copy
Edit
{
  "name": "Ravi Kumar",
  "email": "ravi@gmail.com"
}
✅ Update Attendee Email
Method: PUT

URL: http://127.0.0.1:8000/api/attendees/3/update-email/

Headers:

Content-Type: application/json

Body:

json
Copy
Edit
{
  "email": "newemail@gmail.com"
}
✅ Get Attendees for an Event
Method: GET

URL: http://127.0.0.1:8000/api/events/1/attendees

