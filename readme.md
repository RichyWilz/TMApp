Here's the updated **README** with the additional instructions for Admin account creation:

---

# Task Management Application

## Overview

The **Task Management Application** is a web-based app built with Django that helps manage tasks, with three distinct user roles: **Admin**, **Task Manager**, and **Task Executor**. This application allows users to register, log in, and perform actions based on their assigned roles.

## Features

- **User Registration & Login**: 
  - Users can register an account, and after registering, they can log in.
  - Newly registered users have no roles until an **Admin** assigns one.
  - The system automatically logs users out after 15 minutes of inactivity to improve security.

- **Roles & Permissions**:
  - **Admin**:
    - Can navigate to the admin dashboard (via `/admin`) and log in using admin credentials.
    - Can view, assign roles, and approve registered users.
    - Can assign roles to users (Admin, Task Manager, Task Executor).
  - **Task Manager**:
    - Can create, update, and delete tasks.
    - Can assign tasks to Task Executors.
    - Can view all tasks in the system.
  - **Task Executor**:
    - Can view tasks that are assigned to them.
    - Can mark tasks as complete once done.
  
- **Access Control**: 
  - Only logged-in users can access various views and URLs.
  - Unauthenticated users are restricted from accessing any URL paths that require authentication.

- **Session Timeout**: 
  - Users are automatically logged out after 15 minutes (900 seconds) of inactivity to ensure security.

## Admin Dashboard

Admins can access the **Admin Dashboard** by navigating to `http://127.0.0.1/admin`. From there, they can:

- View a list of registered users.
- Assign roles (Admin, Task Manager, or Task Executor) to new users.
- Approve current users who have not yet been assigned roles.

## Admin Account Creation

To create an **Admin** account, you need to run the following command:

```bash
python manage.py createsuperuser
```

Follow the prompts to provide the necessary details (username, email, password) to create an admin account. Once the admin user is created, you can log in to the admin dashboard at `http://127.0.0.1/admin`.

## System Architecture

- Built using **Django** as the web framework.
- Includes a database model to store user information, tasks, and user roles.
- Implements **user authentication** and **session management**.

## How to Use

1. **Register**: 
   - Navigate to the app's registration page, provide the necessary information, and submit the form.
   
2. **Log In**: 
   - After registration, log in with your credentials. If you're a new user, you will have no role assigned until an Admin grants you one.

3. **Admin Role**: 
   - Once logged in, Admins can manage users by visiting the admin panel at `http://127.0.0.1/admin` and assigning roles.

4. **Task Manager Role**: 
   - Once assigned the **Task Manager** role, you can create, assign, update, and delete tasks for executors.

5. **Task Executor Role**: 
   - Once assigned the **Task Executor** role, you can view tasks assigned to you and mark them as completed when done.

## Technical Requirements

- Python 3.x
- Django 3.x or higher
- Database (SQLite, PostgreSQL, or MySQL)

## Installation

1. Clone the repository.
2. Set up a virtual environment and install the required dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

4. Start the server:

    ```bash
    python manage.py runserver
    ```

5. Visit the app at `http://127.0.0.1:8000`.

## Security Features

- **Session Expiry**: Users are logged out after 15 minutes of inactivity to ensure the safety of their accounts.
- **Password Management**: All users can change their passwords for better security.

## Contributing

Feel free to contribute to the development of this app by submitting pull requests or opening issues for any bugs or feature requests.

---

This **Task Management Application** is designed to be simple, effective, and secure for users to manage tasks and collaborate with ease.