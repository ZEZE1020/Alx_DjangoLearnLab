
## **Social Media API Documentation**

### **Objective**

Develop a Social Media API that enables users to create, view, update, and delete posts and comments. This project also includes user registration and authentication functionalities.

### **Table of Contents**

1. Setup Instructions
2. User Authentication
3. Posts and Comments Functionality
4. Follow System and Feed Functionality
5. API Endpoints
6. Testing and Validation
7. Documentation

## **1. Setup Instructions**

### **Environment Setup**

1. **Clone the Repository**
    * `git clone https://github.com/yourusername/Alx_DjangoLearnLab.git`
    * `cd Alx_DjangoLearnLab/social_media_api`
2. **Create and Activate a Virtual Environment**
    * `python -m venv venv`
    * `source venv/bin/activate` (On Windows, use `venv\Scripts\activate`)
3. **Install the Required Packages**
    * `pip install django djangorestframework psycopg2-binary`
4. **Create and Configure PostgreSQL Database**
    * Create a new PostgreSQL database and user.

Update `settings.py` to include the database configuration: \
python \
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': 'yourdbname',

        'USER': 'yourdbuser',

        'PASSWORD': 'yourdbpassword',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}

    * 
5. **Run Migrations**
    *`python manage.py makemigrations`
    * `python manage.py migrate`
6. **Create a Superuser**
    *`python manage.py createsuperuser`
7. **Start the Development Server**
    * `python manage.py runserver`

## **2. User Authentication**

### **Custom User Model**

The custom user model includes additional fields such as `bio`, `profile_picture`, and `followers`.

#### **Logic**

The `CustomUser` model extends Django's `AbstractUser`, adding fields for user bio, profile picture, and a many-to-many relationship for followers. This enables users to follow each other.

#### **How to Test**

* **Register a New User**: Use a POST request to the `/api/accounts/register/` endpoint with the required user details.
* **Login**: Use a POST request to the `/api/accounts/login/` endpoint with the username and password.
* **Validate**: Ensure a token is returned upon successful registration and login.

## **3. Posts and Comments Functionality**

### **Models**

The `Post` model includes fields such as author, title, content, created_at, and updated_at. The `Comment` model includes fields for referencing a post, author, content, created_at, and updated_at.

#### **Logic**

* **Posts**: Users can create, view, update, and delete posts.
* **Comments**: Users can create, view, update, and delete comments on posts.

#### **How to Test**

* **Create a Post**: Use a POST request to the `/api/posts/` endpoint with the post details.
* **View Posts**: Use a GET request to the `/api/posts/` endpoint.
* **Update a Post**: Use a PUT request to the `/api/posts/{id}/` endpoint with the updated post details.
* **Delete a Post**: Use a DELETE request to the `/api/posts/{id}/` endpoint.
* **Create a Comment**: Use a POST request to the `/api/comments/` endpoint with the comment details.
* **View Comments**: Use a GET request to the `/api/comments/` endpoint.
* **Update a Comment**: Use a PUT request to the `/api/comments/{id}/` endpoint with the updated comment details.
* **Delete a Comment**: Use a DELETE request to the `/api/comments/{id}/` endpoint.

## **4. Follow System and Feed Functionality**

### **Follow System**

#### **Logic**

* **Following**: Users can follow other users, creating a many-to-many relationship between users.
* **Unfollowing**: Users can unfollow other users, removing the relationship.

#### **How to Test**

* **Follow a User**: Use a POST request to the `/api/accounts/follow/{user_id}/` endpoint.
* **Unfollow a User**: Use a POST request to the `/api/accounts/unfollow/{user_id}/` endpoint.

### **Feed Functionality**

#### **Logic**

The feed displays posts from users that the current user follows, ordered by creation date.

#### **How to Test**

* **View Feed**: Use a GET request to the `/api/feed/` endpoint. Ensure it returns posts from users the current user follows, ordered by most recent.

## **5. API Endpoints**

### **User Authentication**

* **Register**: `POST /api/accounts/register/`

Request Body: \
json \
{

  "username": "testuser",

  "password": "testpassword",

  "email": "<testuser@example.com>"

}

    * 

Response: \
json \
{

  "id": 1,

  "username": "testuser",

  "email": "<testuser@example.com>"

}

    * 

* **Login**: `POST /api/accounts/login/`

Request Body: \
json \
{

  "username": "testuser",

  "password": "testpassword"

}

    * 

Response: \
json \
{

  "token": "your-auth-token",

  "user_id": 1,

  "email": "<testuser@example.com>"

}

    * 

### **Posts**

* **List Posts**: `GET /api/posts/`
* **Create Post**: `POST /api/posts/`
* **Retrieve Post**: `GET /api/posts/{id}/`
* **Update Post**: `PUT /api/posts/{id}/`
* **Delete Post**: `DELETE /api/posts/{id}/`

### **Comments**

* **List Comments**: `GET /api/comments/`
* **Create Comment**: `POST /api/comments/`
* **Retrieve Comment**: `GET /api/comments/{id}/`
* **Update Comment**: `PUT /api/comments/{id}/`
* **Delete Comment**: `DELETE /api/comments/{id}/`

### **Follow System**

* **Follow a User**: `POST /api/accounts/follow/{user_id}/`

Response: \
json \
{

  "status": "success",

  "message": "You are now following username"

}

    * 

* **Unfollow a User**: `POST /api/accounts/unfollow/{user_id}/`

Response: \
json \
{

  "status": "success",

  "message": "You have unfollowed username"

}

    * 

### **Feed**

* **View Feed**: `GET /api/feed/`

Response: \
json \
[

  {

    "id": 1,

    "author": "username",

    "title": "Post title",

    "content": "Post content",

    "created_at": "2023-01-01T12:00:00Z",

    "updated_at": "2023-01-01T12:00:00Z"

  },

  ...

]

    * 

## **6. Testing and Validation**

### **Testing Guidelines**

* **Postman**: Use Postman or a similar tool to send requests to the API endpoints and validate the responses.
* **Automated Tests**: Implement automated tests to ensure the endpoints work as expected and that permissions are enforced.

### **Validation**

* **User Authentication**: Ensure tokens are generated and authenticated correctly.
* **Posts and Comments**: Validate CRUD operations for posts and comments.
* **Follow System**: Confirm that users can follow/unfollow others and that the relationship is updated accordingly.
* **Feed**: Verify that the feed displays posts from followed users in the correct order.
