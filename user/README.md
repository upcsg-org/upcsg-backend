# User Authentication API

This document outlines the authentication endpoints available in the User app.

## Authentication Endpoints

### Registration

- **URL:** `/api/user/registration/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "email": "user@example.com",
    "password1": "strongpassword123",
    "password2": "strongpassword123"
  }
  ```
- **Response Body:**
  ```json
  {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI...",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI...",
    "user": {
      "id": 1,
      "email": "user@example.com",
      "image_url": null,
      "bio": null,
      "phone_number": null,
      "date_of_birth": null,
      "first_name": "",
      "last_name": ""
    }
  }
  ```

### Login

- **URL:** `/api/user/login/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "email": "user@example.com",
    "password": "strongpassword123"
  }
  ```
- **Response Body:**
  ```json
  {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI...",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI...",
    "user": {
      "id": 1,
      "email": "user@example.com",
      "image_url": null,
      "bio": null,
      "phone_number": null,
      "date_of_birth": null,
      "first_name": "",
      "last_name": ""
    }
  }
  ```

### Logout

- **URL:** `/api/user/logout/`
- **Method:** `POST`
- **Headers:** 
  ```
  Authorization: Bearer <access_token>
  ```
- **Request Body:** 
  ```json
  {
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI..."
  }
  ```
- **Response Body:**
  ```json
  {
    "detail": "Successfully logged out."
  }
  ```

### Token Refresh

- **URL:** `/api/user/token/refresh/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI..."
  }
  ```
- **Response Body:**
  ```json
  {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI..."
  }
  ```

### Password Reset

- **URL:** `/api/user/password/reset/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "email": "user@example.com"
  }
  ```
- **Response Body:**
  ```json
  {
    "detail": "Password reset e-mail has been sent."
  }
  ```

### Password Reset Confirm

- **URL:** `/api/user/password/reset/confirm/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "uid": "MQ",
    "token": "5jz-a40d78c0ad259a7e763e",
    "new_password1": "newstrongpassword123",
    "new_password2": "newstrongpassword123"
  }
  ```
- **Response Body:**
  ```json
  {
    "detail": "Password has been reset with the new password."
  }
  ```

### Password Change

- **URL:** `/api/user/password/change/`
- **Method:** `POST`
- **Headers:** 
  ```
  Authorization: Bearer <access_token>
  ```
- **Request Body:**
  ```json
  {
    "old_password": "strongpassword123",
    "new_password1": "newstrongpassword123",
    "new_password2": "newstrongpassword123"
  }
  ```
- **Response Body:**
  ```json
  {
    "detail": "New password has been saved."
  }
  ```

### User Details

- **URL:** `/api/user/user/`
- **Method:** `GET`
- **Headers:** 
  ```
  Authorization: Bearer <access_token>
  ```
- **Response Body:**
  ```json
  {
    "id": 1,
    "email": "user@example.com",
    "image_url": null,
    "bio": null,
    "phone_number": null,
    "date_of_birth": null,
    "first_name": "",
    "last_name": ""
  }
  ```

## Authentication Flow

1. Register a new user account using the registration endpoint
2. Log in using the login endpoint to receive access and refresh tokens
3. Use the access token in the Authorization header for authenticated requests
4. When the access token expires, use the refresh token to get a new access token
5. Log out by using the logout endpoint with the refresh token

## Note on Security

- Access tokens are valid for 30 minutes
- Refresh tokens are valid for 7 days
- All authentication requests should be made over HTTPS in production 