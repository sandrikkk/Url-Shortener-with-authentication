## მოცემულ Repository - ში არის სამივე ამოცანის ამოხსნა და პროექტი ! 




## URL Shortener API

Project consists to allow a user to transform a long web url into a pattern-consistent (encoded) small url easy to share and remember.

At the same time the user is allowed to transform back (decode) the small url into the original url

It is partly tested as only and was developed as showcase only.

How Url Shortener API Works:

You can send (POST) a full url and retrieve a small encoded one with tier.app as the base web service url.


Eg. POST http://127.0.0.1:8000/api/short-url/ with https://www.google.com/search?q=google&oq=google+&aqs result: http://127.0.0.1:8000/api/upxFJp (6 digits id)

You can get the original url with the encoded url on a GET request (done in previous step)

Eg. GET http://127.0.0.1:8000/api/upxFJp result: https://www.google.com/search?q=google&oq=google+&aq

I used JWT authentication to create a custom user and then checked whether the user had premium permission or not.
 
Firstly, you need to create a user or superuser. Then, navigate to this URL: http://127.0.0.1:8000/api/user/login/. You will need to enter the email and password, and upon sending a POST request, you will receive a result similar to this example:
<br />
```
{
"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3OTA0NTA2NywiaWF0IjoxNjc4OTU4NjY3LCJqdGkiOiI2NmJiZmJhNjg4NDk0OTc4OGYxZGJhYjdlZWMzZDczNyIsInVzZXJfaWQiOjF9.XNrsZG-5rvkCO4gvGTA5gG0Jhww1fJ48I_iayJVf2CA",
"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNTUwNjY3LCJpYXQiOjE2Nzg5NTg2NjcsImp0aSI6ImIxZDgzYzAzOWM2MTRhODA4ZGZjNGQxOTg1M2I5OTJmIiwidXNlcl9pZCI6MX0.eDr7eijdjMUV8Ftvfc07sOu1GWK8MSthSFYCcd6j48k",
"id": 1,
"_id": 1,
"email": "iashvilisandro7@gmail.com",
"name": "Sandro Iashvili",
"is_staff": true,
"is_premium": true,
"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNTUwNjY3LCJpYXQiOjE2Nzg5NTg2NjcsImp0aSI6IjNkZGI1NDA0ZDAyYjQzMTg4MDcwYmM5MDQxZDIxM2FkIiwidXNlcl9pZCI6MX0.-I8V12PhZIyXMiGDxvhPiJLaY4TdAS-uB5GQYWmsUjI"
}
```

## Installation:
1) Clone repository and go inside the repository folder "url-shortener-api"

```
git clone https://github.com/sandrikkk/URL-Shortener-API.git
```

2) Create you virtualenv and install the packages

```
pip install -r requirements.txt
```

3) Initialize database and create the database mapping used for persistance in the url shortener API.

```
python manage.py makemigrations
```

4) Apply the database mapping from the app to the database; migrate the database.

```
python manage.py migrate
```

5)Run the application.
```
python manage.py runserver
```

<br>

## USAGE
#### 1. Endpoint List

URL Example: `http://127.0.0.1:8000/api/short-url/`

#### 1. when is_premium = True

INPUT POST REQUEST:
```
{
    "original_link":"https://sweeftdigital.com/",
    "custom_url": "sweeft",
}
```

OUTPUT GET REQUEST:
```
{
    "id": 147,
    "original_link": "https://sweeftdigital.com/",
    "shortened_link": "http://127.0.0.1:8000/api/sweeft/",
    "created_at": "2023-03-16T09:29:06.139840Z",
    "count": 0,
    "is_premium": true,
    "custom_url": "sweeft"
}
```

#### 2. when is_premium = False

INPUT POST REQUEST:
```
{
    "original_link":"https://sweeftdigital.com/",
    "custom_url": "sweeft",
}
```

OUTPUT GET REQUEST:
```
{
    "id": 148,
    "original_link": "https://sweeftdigital.com/",
    "shortened_link": "http://127.0.0.1:8000/api/tzXFHV/",
    "created_at": "2023-03-16T09:32:21.551781Z",
    "count": 0,
    "is_premium": false,
    "custom_url": "sweeft"
}
```


| | Available Methods | URI | Example URL |
| -: | :- | :- | -: |
| | | | |
| | **Project Endpoints** | | |
| 1. | `POST` | `/api/short-url/` | `http://127.0.0.1:8000/api/short-url/` |
| 2. | `GET`  | `/api/short-url/<id>/` | `http://127.0.0.1:8000/api/short-url/<id>/` |
| 3. | `DELETE`  | `/api/short-url/<id>/` | `http://127.0.0.1:8000/api/short-url/<id>` |
| 4. | `POST`  | `/api/user/login/` | `http://127.0.0.1:8000/api/user/login/>` |


<br>
