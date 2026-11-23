# Daily Activity Tracker

A simple full-stack web application for recording, managing, and tracking daily activities. Users can create activity entries, organize them by category, update their status, and view activity statistics.

## Features

- Create daily activity entries
- View recorded activities
- Update existing entries
- Delete entries
- Organize activities by category
- Track completion status
- Add notes to activities
- View activity statistics

## Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript

**Backend**
- Python
- FastAPI
- SQLAlchemy

**Database**
- PostgreSQL

## Project Structure

```text
daily-activity-tracker/
├── backend/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   └── script.js
├── .gitignore
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API health |
| GET | `/entries` | Retrieve activity entries |
| POST | `/entries` | Create an activity entry |
| PUT | `/entries/{id}` | Update an activity entry |
| DELETE | `/entries/{id}` | Delete an activity entry |
| GET | `/stats` | Retrieve activity statistics |

## Requirements

- Python 3.10+
- PostgreSQL
- pip

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/keerthana0325/daily-activity-tracker.git
cd daily-activity-tracker
```

### 2. Install backend dependencies

```bash
pip install -r backend/requirements.txt
```

### 3. Configure the database

Ensure PostgreSQL is running and create the `habit_db` database.

Create a `.env` file in the project root and configure your database connection:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost/habit_db
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

**Do not commit the `.env` file.**

### 4. Run the backend

From the project root:

```bash
python -m uvicorn backend.main:app --reload
```

### 5. Access the application

Open `frontend/index.html` in your browser to access the frontend.

The backend API is available at:

`http://127.0.0.1:8000`

Interactive API documentation is available at:

`http://127.0.0.1:8000/docs`

## Future Improvements

- Input validation and error handling
- Improved frontend interaction and user experience
- Automated testing
- Additional activity analytics
