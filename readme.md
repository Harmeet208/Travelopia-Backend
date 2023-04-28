# Travelopia Assignment - Backend

## Available Scripts

Before running this project - 

### Please make sure that you are using the correct versions

For python - 3.11.3
For pip - 23.1
For PostgreSQL - 15.2 

## Changes to make

1. Navigate to `backend` Directory
2. Now inside settings.py file change the database credentials to create tables locally, which looks like - 
    Line Number - 79 -> DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


## In the project directory, you can run:

### 1. `pip install -r requirements.txt`

To install the required python dependencies

### 2. ` python manage.py migrate`

After installing the packages, run the above command to create the required tables

### 3. ` python manage.py runserver`

After tables have been created, to launch the project run the above command

### By default project runs on http://127.0.0.1:8000/
