
**Authentication Features Overview**

**1. Custom User Model**



* The project uses a custom user model, `CustomUser`, which extends `AbstractUser`. This model includes additional fields like `bio` and `profile_picture` to store user-specific information.
* Located in `accounts/models.py`.

**2. User Registration and Login**



* The API provides endpoints for user registration and login.
* **Registration**: Allows new users to create an account by providing a username, email, and password.
* **Login**: Allows existing users to obtain an authentication token by providing their username and password.

**3. Token-Based Authentication**



* The project uses Django REST Framework’s token-based authentication.
* Users receive a token upon successful login, which must be included in the Authorization header for subsequent API requests.

**Endpoints**:



* **Registration**: `POST /api/accounts/register/`
* **Login**: `POST /api/accounts/login/`

**Testing Authentication Features**

**1. User Registration**



* **Endpoint**: `POST /api/accounts/register/`

**Request Body**: \
json \
{

  "username": "testuser",

  "email": "testuser@example.com",

  "password": "password123"

}



* 

**Expected Response**: \
json \
{

  "id": 1,

  "username": "testuser",

  "email": "testuser@example.com",

  "bio": null,

  "profile_picture": null

}



* 

**2. User Login**



* **Endpoint**: `POST /api/accounts/login/`

**Request Body**: \
json \
{

  "username": "testuser",

  "password": "password123"

}



* 

**Expected Response**: \
json \
{

  "token": "your-auth-token"

}



* 

**3. Token-Based Authentication**



* Include the token in the `Authorization` header for API requests that require authentication.

**Header**: \
plaintext \
Authorization: Token your-auth-token



* 

**Example Test Scenario**:



1. **Register a New User**:
    * Use a tool like Postman or cURL to send a `POST` request to the registration endpoint.
    * Verify that the response contains the user details.
2. **Login with the Registered User**:
    * Send a `POST` request to the login endpoint with the registered user’s credentials.
    * Verify that the response contains the authentication token.
3. **Access Protected Endpoint**:
    * Use the token to access a protected endpoint (e.g., user profile).
    * Include the token in the `Authorization` header and verify that the request succeeds.