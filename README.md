# API_service_for_theater #

The **API_service_for_theater** is a Django REST Framework-based application for managing theatre-related data, including actors, genres, plays, theatre halls, performances, reservations, and tickets. This API supports CRUD operations for all models and is fully integrated with PostgreSQL.

---

## Features

- **Actors**: Manage actors with their first and last names.
- **Genres**: Categorize plays into genres.
- **Plays**: Store information about plays with descriptions and associated actors and genres.
- **Theatre Halls**: Define halls with rows and seats.
- **Performances**: Schedule play performances in theatre halls.
- **Reservations**: Handle user reservations for performances.
- **Tickets**: Issue tickets with seat and row information for specific performances.

---

## Technologies Used

- **Django**: Backend framework.
- **Django REST Framework (DRF)**: API development.
- **PostgreSQL**: Database.

---

## Installation and Setup

### Prerequisites

- Python 3.8+
- PostgreSQL 12+

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/iishchenko/API_service_for_theater
   cd theatre_api
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**:
   Update the `DATABASES` section in `theatre_api/settings.py` with your PostgreSQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the API**:
   Visit `http://127.0.0.1:8000/api/` in your browser or use an API client like Postman.

---

## API Endpoints

### Actors
- `GET /api/actors/`: List all actors.
- `POST /api/actors/`: Create a new actor.

### Genres
- `GET /api/genres/`: List all genres.
- `POST /api/genres/`: Create a new genre.

### Plays
- `GET /api/plays/`: List all plays.
- `POST /api/plays/`: Create a new play.

### Theatre Halls
- `GET /api/halls/`: List all theatre halls.
- `POST /api/halls/`: Create a new theatre hall.

### Performances
- `GET /api/performances/`: List all performances.
- `POST /api/performances/`: Schedule a new performance.

### Reservations
- `GET /api/reservations/`: List all reservations.
- `POST /api/reservations/`: Create a new reservation.

### Tickets
- `GET /api/tickets/`: List all tickets.
- `POST /api/tickets/`: Create a new ticket.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Typical commands

 docker-compose up --build
 docker-compose up test  --build
 docker-compose down