# PROGRAMMING COURSES PLATFORM

# OVERVIEW
This project is a web-based platform that allows users to access programming courses. Users can perform various actions such as logging in, logging out, signing up, and viewing their profiles. The courses are presented with detailed information, and users can enroll in them through YOUTUBE.

## FEATURES
### User Authentication:

- Users can sign up with a valid email address, username, and password.
- Secure authentication using password hashing.
- Existing users can log in with their credentials.

### User Profile:

- Users have personalized profiles.
- Profile includes email, username, and an option to upload a profile picture.

### Course Display:

- Courses are displayed with relevant details, such as course name, duration, and description.
- Courses are visually appealing with images and additional information.

### Enrollment:

- Users can enroll in courses by clicking the "Enroll Now" button, after clicking on the "Enroll Now" button it moves you a youtube course depending on t course you've chosen to enroll.

### Flash Messages:

- Informative flash messages are displayed for user actions, such as successful login, invalid password, and more.

## Technologies Used
### Frontend:

- HTML, CSS
- Bootstrap 5.3.2
- JavaScript (jQuery)

### Backend:
- Python (Flask)
- SQLAlchemy for database interaction
- Flask-Login for user authentication

### Database:
- SQLite (can be easily changed to another database as needed)

### Project Structure
- static/: Contains static files such as CSS, images, and JavaScript.
- templates/: Contains HTML templates for different pages.
- website/: Python package for the Flask application.
    - __init__.py: Initializes the Flask application.
    - models.py: Defines the database models (User).
    - views/: Contains blueprints for different views (auth, views).
        - auth.py: Handles user authentication (login, logout, signup).
        - views.py: Manages general views (home, profile, course display).

## Setup
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies using pip install -r requirements.txt.
4. Run the application with python main.py.

>[!NOTE]
> The application will be accessible at http://localhost:5000/.
