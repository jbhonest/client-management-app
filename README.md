# Django Client Management App

This is a simple Django web application for managing clients. The app allows you to view a list of clients and add new clients.

## Features

- View a list of clients
- Add new clients
- Displays client's full name and email

## Models

### Client

- `first_name`: CharField (max_length=255)
- `last_name`: CharField (max_length=255)
- `email`: EmailField (unique=True)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/django-client-app.git
    cd django-client-app
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

6. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:8000/clients/
    ```

## Project Structure

