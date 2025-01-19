# Codeleap API

This repository contains the implementation of a backend API using Django, developed to manage user posts on a platform. The API is designed to support CRUD operations (Create, Read, Update, Delete) for posts.

### Features:
- **GET**: List all posts.
- **POST**: Create new posts.
- **PATCH**: Partially update an existing post.
- **DELETE**: Delete a post.

### Data Structure:
The API handles the following data structure for each post:

```json
{
    "id": "number",
    "username": "string",
    "created_datetime": "datetime",
    "title": "string",
    "content": "string"
}

````
### Deploy
The API is hosted and accessible at the following link:  
[Codeleap API - Posts](https://codeleap-z2f1.onrender.com/api/posts/)

### Technologies Used:
- Django
- Django REST Framework
- CORS Headers to allow requests from different origins

### Running the Project Locally:
1. Clone this repository.
2. Install the dependencies: `pip install -r requirements.txt`.
3. Apply the migrations: `python manage.py migrate`.
4. Start the server: `python manage.py runserver`.