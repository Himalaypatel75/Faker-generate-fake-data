# Django Fake Data Generator

This Django project generates fake data based on user-selected fields using the Faker library. Users can select multiple fields and specify the number of records to generate, all through a user-friendly web interface enhanced with Bootstrap.

## Features

- Select from 20 different data fields to generate fake data (e.g., name, email, phone number, etc.).
- Specify the number of records to generate (between 1 and 100).
- Beautiful and responsive UI built with Bootstrap 4.
- Display generated data in a neatly formatted table.

## Demo

Here's how the application looks:

### Main Page
![Main Page](https://github.com/Himalaypatel75/Faker-generate-fake-data/blob/main/Screenshot%20from%202024-08-23%2022-48-09.png)

### Generated Data
![Generated Data](https://github.com/Himalaypatel75/Faker-generate-fake-data/blob/main/Screenshot%20from%202024-08-23%2022-48-09.png)

## Prerequisites

- Python 3.x
- Django 3.x or later
- Faker library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Himalaypatel75/Faker-generate-fake-data.git
    cd Faker-generate-fake-data
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Django development server:**

    ```bash
    python manage.py runserver
    ```

5. **Visit the application in your browser:**

    Go to `http://127.0.0.1:8000/` to use the Fake Data Generator.

## Usage

1. Select the fields you want to generate from the list of options.
2. Enter the number of records you want to generate.
3. Click "Generate Data" to see the results in a table.

## Project Structure

