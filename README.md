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

## 📌 API Endpoints

| Method | Endpoint                                     | Description                         |
| ------ | -------------------------------------------- | ----------------------------------- |
| POST   | `/api/events`                                | Create an event                     |
| GET    | `/api/events/`                               | List upcoming events                |
| POST   | `/api/events/<event_id>/register`            | Register an attendee for an event   |
| GET    | `/api/events/<event_id>/attendees`           | List attendees for a specific event |
| PUT    | `/api/attendees/<attendee_id>/update-email/` | Update attendee's email             |

---

