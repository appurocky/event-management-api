
# Event Management API

An API built with Django and Django REST Framework for creating and managing events and attendees.

---

## Features

- Create and list events  
- Register attendees for specific events  
- View attendees of a specific event  
- Auto-generated API docs with Swagger and Redoc  

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

5. **Access the API Docs**
   - Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
   - ReDoc UI: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## API Endpoints

| Method | Endpoint                            | Description                        |
|--------|-------------------------------------|------------------------------------|
| POST   | /api/events                         | Create an event                    |
| GET    | /api/events/                        | List upcoming events               |
| POST   | /api/events/<event_id>/register     | Register attendee for an event     |
| GET    | /api/events/<event_id>/attendees    | List attendees of an event         |

---

## Sample API Calls (Plain Format)

### Create Event

**Method:** POST  
**URL:** `http://127.0.0.1:8000/api/events`  
**Headers:**
```
Content-Type: application/json
```
**Body:**
```json
{
  "name": "Tech Conference",
  "start_time": "2025-07-01T18:00:00Z",
  "end_time": "2025-07-01T21:00:00Z",
  "max_attendees": 100
}
```

---

###  List Upcoming Events

**Method:** GET  
**URL:** `http://127.0.0.1:8000/api/events/`

---

### Register Attendee for Event

**Method:** POST  
**URL:** `http://127.0.0.1:8000/api/events/<event_id>/register`  
**Headers:**
```
Content-Type: application/json
```
**Body:**
```json
{
  "name": "Aravind",
  "email": "aravindappu997@gmail.com"
}
```

---

### 👥 List Attendees of Event

**Method:** GET  
**URL:** `http://127.0.0.1:8000/api/events/<event_id>/attendees`
