# Event Management System

## Overview
The Event Management System is a web application built using Django that allows users to manage events, participants, and categories. The application provides a user-friendly interface for creating, reading, updating, and deleting events and participants, as well as viewing detailed information about each event.

## Features
- Create, Read, Update, and Delete (CRUD) operations for events, participants, and categories.
- Optimized database queries using Django's ORM.
- Responsive front-end design using Tailwind CSS.
- Organizer dashboard with statistics and today's events listing.
- Search functionality to find events by name or location.

## Installation

### Prerequisites
- Python 3.x
- Django
- Node.js and npm (for front-end dependencies)

### Setup
1. Clone the repository:
   ```
   git clone <repository-url>
   cd event_management
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Install front-end dependencies:
   ```
   npm install
   ```

5. Run migrations to set up the database:
   ```
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

8. Access the application at `http://127.0.0.1:8000/`.

## Usage
- Navigate to the admin panel to manage events, participants, and categories.
- Use the organizer dashboard to view statistics and today's events.
- Utilize the search feature to find events by name or location.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.