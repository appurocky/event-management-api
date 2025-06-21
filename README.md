## Setup Instructions

---

##  Features

- Create and list events  
- Register attendees for specific events  
- View attendees of a specific event  
- Auto-generated API docs with Swagger and Redoc

---

1. **Clone the Repository**
   ```bash
   git clone https://github.com/appurocky/event-management-api.git
   cd event-management-api ```
   
2. **Install Dependencies**
	```pip install django
	pip install djangorestframework
	pip install drf-yasg```

3. **Run Migrations**
    ```python manage.py makemigrations
    python manage.py migrate```

4. **Start the Development Server**
    ```python manage.py runserver```

5. **Access the API**
	```Swagger UI: http://127.0.0.1:8000/swagger/

	   ReDoc UI: http://localhost:8000/redoc/```


## API Endpoints

1. **Create an Event**
  ```POST /api/events```
  
2. **List Upcoming Events**
  ```GET /api/events/```
  
3. **Register an Attendee for an Event**
  ```POST /api/events/<event_id>/register```
  
4. **List Attendees for an Event**
   ```GET /api/events/<event_id>/attendees```
