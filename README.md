# Django User Authentication App

A simple Django-based user authentication system featuring user registration, login, and a secure dashboard. This project uses Django's built-in authentication system with custom forms and models for a streamlined user experience.

## Features

1. **User Registration**:
   - Users can register with a username and password.
   - Form validation ensures proper input before saving user details to the database.
   - Redirects to the login page upon successful registration.

2. **User Login**:
   - Users can log in with valid credentials.
   - Authenticates users using Django's `authenticate` function.
   - Redirects authenticated users to a secure dashboard.

3. **Secure Dashboard**:
   - Dashboard accessible only to logged-in users.
   - Protected with the `@login_required` decorator to ensure security.

4. **Homepage**:
   - A welcoming homepage serves as the app's entry point.

5. **Routing**:
   - Organized URLs to handle registration, login, and dashboard functionality.

6. **Templates**:
   - HTML templates for a clean and simple user interface:
     - `index.html`: Homepage.
     - `register.html`: Registration page.
     - `my_login.html`: Login page.
     - `dashboard.html`: Secure dashboard.

## Installation and Setup

### Prerequisites
- Python 3.8+
- Django 4.2+
- Virtual environment (optional but recommended)

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Volcann/E-learning-Site.git
   cd <repository-folder>
