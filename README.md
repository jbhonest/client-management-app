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


## Usage

### Viewing Clients

Navigate to `http://127.0.0.1:8000/clients/` to view the list of clients.

### Adding Clients

Navigate to `http://127.0.0.1:8000/clients/add/` to add a new client. Fill out the form and submit to add the client to the database.

## Code Overview

### Models

The `Client` model represents a client with a first name, last name, and unique email address. It includes a method to get the full name of the client.

### Views

- `client_list` - Displays the list of clients.
- `add_client` - Displays a form to add a new client.

### Forms

- `ClientForm` - A ModelForm for the `Client` model.

### URLs

- `clients/` - URL for the client list view.
- `clients/add/` - URL for the add client view.

### Templates

- `client_list.html` - Template for displaying the list of clients.
- `add_client.html` - Template for the form to add a new client.


---

Developed by Jamal Badiee (jbhonest@yahoo.com)


