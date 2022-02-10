# Project - Event Management Web Application based on Django Framework
## Getting Started

## About this project:
A dynamic event management project developed using the popular python framework "Django". The templates
used in the project from the bootstrap. This project mainly focus on exploring the various feautures 
available in the djnago framework

Thie web app provide exciting feautues where an user with admin access can add venues, create events and manage them. This app also allow users to downlaod the venues and events data as portable files like
excel,pdf and text file.



## Running The code 
  
  ### Dependencies Required for the project
      asgiref==3.5.0
      backports.zoneinfo==0.2.1
      Django==4.0.2
      sqlparse==0.4.2

  ### How to run
    1. To install the virtual environment - python3 -m venv envname // on linux 
    2. Checking django version: python -m django --version
    3. Installing django: python -m pip install Django
    4. To run the app- from the project folder: python manage.py runserver
       Also, to change the port: python manage.py runserver 8080


## Components of the App:

#### This project contains three different apps
#### 1. events- This app contains the imlentation of the events and venues and performing CRUD operations.
#### 2. members- This is another app which is responsible to apply the user authentication system which allows an user to register, login, handles appropriates rights given to an user.
#### 3. files- This handles request for viewing or downloading the contents of the events, venues, etc in portable file formats like pdf, excel file, txt file

