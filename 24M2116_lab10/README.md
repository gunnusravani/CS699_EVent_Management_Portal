# Event Management Portal
This is a Flask-based Event Management Portal that allows users to register for events and provides event hosts with a dashboard to manage their events. The application includes features tailored for both regular users and hosts, ensuring an intuitive interface and a user-friendly experience.


# Project Team Details
1) Team Name : Load Balancers
2) Team Members :
  -   Sravani Gunnu (24M2116)
  -   Russel Abreo (24M2107)
  -   Atharv Shingewar (24M0834)

# Directory Structure
This project is packaged as 24M2116_lab10.tar.gz. The tar file contains the following folders:

-    24M2116_lab10/
-    ├── Flask_Project/                    -----  # Contains the main application
-    │   ├── app/
-    │   │   ├── templates/                -----   # HTML templates
-    │   │   ├── static/                   -----  # Static files (CSS, images)
-    │   │   ├── __init__.py               -----  # Initialize Flask application
-    │   │   └── routes.py                 -----  # Main application routes
-    │   ├── run.py                        -----  # Flask entry point
-    │   └── requirements.txt              -----  # Dependencies
-    ├── screenshots/                      -----  # Application screenshots
-    |
-    └── README.md                         -----  # Project documentation (this file)



# Features
## User Authentication:

Users can log in with unique email addresses (10 sample users provided).
Hosts (3 sample Gmail addresses) can log in with special privileges.
## Event Registration:

Users can view and register for upcoming events.
Each user is limited to one registration per event.
Hosts cannot register for their own events.
## Host Dashboard:

Hosts can access a host-specific dashboard showing events they are managing.
Hosts can view a list of users registered for each of their events.
## Event Display with Images:

Event detail pages show a unique image for each event.
The login page has a blurred, semi-transparent background image.

# Setup Instructions

## Extract the Project:
- tar -xzf 24M2116_lab10.tar.gz
- cd 24M2116_lab10/Flask_Project
## Create a Virtual Environment:
- python3 -m venv venv
## Activate the Virtual Environment:
- source venv/bin/activate
## Install Dependencies:
- pip install -r requirements.txt
## Run the Application:
- python3 run.py



# Application Usage
## Login as a User or Host:

- User Examples:  user1@gmail.com to user10@gmail.com, password: password1, password2, etc.
- Host Examples:  host1@gmail.com, host2@gmail.com, host3@gmail.com, with passwords: password1, password2, password3.

## Register for Events:

- Users can view event details and register.
Duplicate registrations are prevented, and hosts cannot register for their own events.
## Host Dashboard:
- Hosts can access the "Host Dashboard" to view events they manage and see a list of registered users for each event.