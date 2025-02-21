Flask RESTful API with MongoDB and JWT Authentication

Project Overview

This project is a RESTful API built using Flask and MongoDB (hosted on MongoDB Atlas). It features JWT-based authentication to ensure that users can only access their own resources. The API includes endpoints for user registration, login, and CRUD operations for managing email templates.

Hosted URL

API is hosted on Render:
https://mail-template-c8qy.onrender.com

Features

User authentication using JWT tokens

MongoDB Atlas as the database

Secure API with token-based authentication

CRUD operations for email templates

Hosted for free on Render

API Endpoints

1. User Registration

URL: /register
Method: POST

Headers:

{
  "Accept": "application/json",
  "Content-Type": "application/json"
}

Body:

{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "password": "password123"
}

2. User Login

URL: /login
Method: POST

Headers:

{
  "Accept": "application/json",
  "Content-Type": "application/json"
}

Body:

{
  "email": "john.doe@example.com",
  "password": "password123"
}

Response:
Returns a JWT access token.

{
  "access_token": "your_jwt_token_here"
}

3. Template CRUD Operations

Insert New Template

URL: /template
Method: POST

Headers:

{
  "Authorization": "Bearer <access_token>",
  "Accept": "application/json",
  "Content-Type": "application/json"
}

Body:

{
  "template_name": "Welcome Email",
  "subject": "Welcome to Our Service!",
  "body": "Thank you for signing up."
}

Get All Templates

URL: /template
Method: GET

Headers:

{
  "Authorization": "Bearer <access_token>",
  "Accept": "application/json"
}

Get Single Template

URL: /template/<template_id>
Method: GET

Headers:

{
  "Authorization": "Bearer <access_token>",
  "Accept": "application/json"
}

Update Template

URL: /template/<template_id>
Method: PUT

Headers:

{
  "Authorization": "Bearer <access_token>",
  "Accept": "application/json",
  "Content-Type": "application/json"
}

Body:

{
  "template_name": "Updated Template",
  "subject": "Updated Subject",
  "body": "Updated email body."
}

Delete Template

URL: /template/<template_id>
Method: DELETE

Headers:

{
  "Authorization": "Bearer <access_token>",
  "Accept": "application/json"
}

Project Structure

app/
│── __init__.py        # Initializes Flask app
│── models.py          # Defines database models
│── templates.py       # Handles template CRUD operations
│── token_utils.py     # JWT token utilities
│── urls.py            # Defines API routes
│── user.py            # User authentication logic
│
├── requirements.txt   # Dependencies
├── run.py             # Application entry point
├── Procfile           # For deployment

Installation

Clone the repository:

git clone <your-repo-url>
cd <your-repo-folder>

Install dependencies:

pip install -r requirements.txt

Run the application:

python run.py

Use Postman to test API endpoints.

Dependencies (requirements.txt)
Flask RESTful API with MongoDB and JWT Authentication

Project Overview

This project is a RESTful API built using Flask and MongoDB (hosted on MongoDB Atlas). It features JWT-based authentication to ensure that users can only access their own resources. The API includes endpoints for user registration, login, and CRUD operations for managing email templates.

Hosted URL

API is hosted on Render:
Live API

Features

User authentication using JWT tokens

MongoDB Atlas as the database

Secure API with token-based authentication

CRUD operations for email templates

Hosted for free on Render

API Endpoints

1. User Registration

URL: /register
Method: POST

Headers:

{
  "Accept": "application/json",
  "Content-Type": "application/json"
}

Body:

{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "password": "password123"
}

2. User Login

URL: /login
Method: POST

Headers:

{
  "Accept": "application/json",
  "Content-Type": "application/json"
}

Body:

{
  "email": "john.doe@example.com",
  "password": "password123"
}

Response:
Returns a JWT access token.

{
  "access_token": "your_jwt_token_here"
}

3. Template CRUD Operations

Insert New Template

URL: /template
Method: POST

Headers:

{
  "Authorization": "Bearer <access_token>",
  "Accept": "application/json",
  "Content-Type": "application/json"
}

Body:

{
  "template_name": "Welcome Email",
  "subject": "Welcome to Our Service!",
  "body": "Thank you for signing up."
}

Get All Templates

URL: /template
Method: GET

Headers:

{
  "Authorization": "Bearer <access_token>",
  "Accept": "application/json"
}

Get Single Template

URL: /template/<template_id>
Method: GET

Headers:

{
  "Authorization": "Bearer <access_token>",
  "Accept": "application/json"
}

Update Template

URL: /template/<template_id>
Method: PUT

Headers:

{
  "Authorization": "Bearer <access_token>",
  "Accept": "application/json",
  "Content-Type": "application/json"
}

Body:

{
  "template_name": "Updated Template",
  "subject": "Updated Subject",
  "body": "Updated email body."
}

Delete Template

URL: /template/<template_id>
Method: DELETE

Headers:

{
  "Authorization": "Bearer <access_token>",
  "Accept": "application/json"
}

Project Structure

app/
│── __init__.py        # Initializes Flask app
│── models.py          # Defines database models
│── templates.py       # Handles template CRUD operations
│── token_utils.py     # JWT token utilities
│── urls.py            # Defines API routes
│── user.py            # User authentication logic
│
├── requirements.txt   # Dependencies
├── run.py             # Application entry point
├── Procfile           # For deployment

Installation

Clone the repository:

git clone <your-repo-url>
cd <your-repo-folder>

Install dependencies:

pip install -r requirements.txt

Run the application:

python run.py

Use Postman to test API endpoints.

Dependencies (requirements.txt)

Flask
Flask-JWT-Extended
Flask-PyMongo
PyJWT
bcrypt
python-dotenv

.env file 

add MONGO_URI=<MONGODB CONNECTION URI>
add SECRET_KEY = <Your Secret_key>
Deployment

The API is deployed on Render. Modify the Procfile if needed:

web: gunicorn run:app

Notes

JWT tokens are used to authenticate requests.

Ensure MongoDB Atlas is properly configured with your connection URI in .env.

All API requests should be tested using Postman.

Author

Vaira Delipan

Deployment

The API is deployed on Render. Modify the Procfile if needed:

web: gunicorn run:app

Notes

JWT tokens are used to authenticate requests.

Ensure MongoDB Atlas is properly configured with your connection URI in .env.

All API requests should be tested using Postman.

Author

Vaira Delipan
