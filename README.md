# Newspaper Project

This is a Django-based news blog application where users can create, edit, and delete articles. The project includes user authentication and role-based permissions (e.g., editors vs. readers).

## Features
- User Authentication (login, registration, logout)
- Role-Based Access Control (Editors can create/edit/delete; Readers can only view and comment)
- Basic CRUD functionality for articles
- Responsive design with basic templates

## Project Structure
- `articles/` - Contains the article model, views, and related migrations.
- `pages/` - Static pages (e.g., homepage, about).
- `users/` - User-related views and models.
- `newspaper_project/` - Main Django project files (settings, URLs, etc.).
- `templates/` - HTML files for the frontend.
- `requirements.txt` - Dependencies for the project.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/newspaper_project.git
    cd newspaper_project
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (for accessing the admin panel):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the server**:
    ```bash
    python manage.py runserver
    ```

## Usage
- Go to `http://127.0.0.1:8000/` to view the homepage.
- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage articles and users.

## License
This project is licensed under the MIT License.
