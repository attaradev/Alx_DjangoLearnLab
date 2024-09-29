# Social Media API

## Setup Instructions

1. Install dependencies: `pip install django djangorestframework`
2. Run migrations: `python manage.py migrate`
3. Start the server: `python manage.py runserver`

## User Registration

- Endpoint: `/register`
- Method: `POST`
- Payload:

  ```json
  {
    "username": "exampleuser",
    "password": "examplepass",
    "bio": "Hello, world!",
    "profile_picture": "image_url"
  }
