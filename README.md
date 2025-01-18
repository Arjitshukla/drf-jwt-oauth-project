# Django DRF with Simple JWT and OAuth2 Authentication

This project is a Django application that implements an API for creating and listing items, secured with Simple JWT (JSON Web Token) and OAuth2 authentication. Follow the steps below to set up and use the project.

 ## Prerequisites

Ensure you have the following installed:

* Python 3.8+

* pip (Python package manager)

* Django 4.0+

* Django REST Framework

* django-oauth-toolkit

## Installation Steps

**1. Clone the Repository**
```base
git clone <repository-url>
cd <repository-directory>
```
**2. Create and Activate a Virtual Environment**
```base
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
**3. Install Dependencies**
```bse
pip install -r requirements.txt
```
Ensure the `requirements.txt` contains:

    Django
    djangorestframework
    djangorestframework-simplejwt
    django-oauth-toolkit

**4. Apply Migrations**
```base
python manage.py makemigrations
python manage.py migrate
```
**5. Create a Superuser (Optional)**
```bse
python manage.py createsuperuser
```
Follow the prompts to set up a superuser account.

## Configuration

*  Add Required Apps in `settings.py`

Ensure the following apps are added:
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'rest_framework_simplejwt',
        'oauth2_provider',
        'mydrfapp',  # Replace with your app name
    ]

*  Configure REST Framework Settings

Add the authentication classes to settings.py:

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
            'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
    }

## Running the Application

**1. Start the Development Server**
```base
python manage.py runserver
```
**2. Access the API Endpoints**

## JWT Authentication Endpoints: 👨‍💻

* Obtain Token: `POST /api/token/`

* Refresh Token: `POST /api/token/refresh/`

Example Request for Token:
```bse
curl -X POST http://127.0.0.1:8000/api/token/ \
    -H "Content-Type: application/json" \
    -d '{"username": "<your-username>", "password": "<your-password>"}'
```
## OAuth2 Authentication Endpoints:👨‍💻

* Authorization URLs: `/o/`

### Item Endpoints:

* List/Create Items: `GET/POST /items/`

## Testing the API

**1. Obtain a Token (JWT or OAuth2)**

Use the provided endpoints to get a valid access token. Pass the token in the Authorization header:
```base
Authorization: Bearer <your-access-token>
```
**2. Test Item List Endpoint**
```bse
curl -X GET http://127.0.0.1:8000/items/ \
    -H "Authorization: Bearer <your-access-token>"
```
**3. Test Item Create Endpoint**
```bse
curl -X POST http://127.0.0.1:8000/items/ \
    -H "Authorization: Bearer <your-access-token>" \
    -H "Content-Type: application/json" \
    -d '{"field1": "value1", "field2": "value2"}'
```
### Deployment Notes

**👉 Environment Variables  :**

Use environment variables to store sensitive information like database credentials and secret keys.

**👉 Security Best Practices  :**

* Use HTTPS in production.

* Rotate tokens and secrets periodically.

* Limit token lifespan for better security.


## Final Note :👨‍💻👨‍💻

Congratulations on setting up your Django project with `JWT and OAuth2` authentication! Remember, every line of code you write brings you one step closer to becoming a master developer. Keep experimenting, learning, and growing. You've got this! 🚀

