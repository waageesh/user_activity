# Django_Projects
design and implement a Django application with User and ActivityPeriod models, write a custom management command to populate the database with some dummy data, and design an API to serve that data in the json format

< pip3 install virtualenv >
create virtualenv for project as 
< virtualenv fullthrottle >
activate the venv by going 
   -- fullthrottle/scripts
and run activate.bat as below
C:\fullthrottle\scripts > activate.bat

After activating the venv,

install django inside virtualenv with below command
< pip install django  >

install REST_FRAMEWORK
< pip install djangorestframework >

After installing django, 
go to main project folder and create new Django site using below command
< django-admin startproject period >

To use PL/SQL as database , 
< pip install psycopg2 > inside Virtualenv

create new app as below
< python runserver startapp app_name >

Add added apps in settings.py(in project folder)
    'rest_framework',
    'activity_period',
add database engine for PL/SQL in settings.py for DATABASES dict variable as below
'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<db_name>',
        'USER': '<username>',
        'PASSWORD':'<db_password>',
        'HOST' : 'localhost',
        'PORT': '',
    }


create model based in given JSON file.
then create serializer.py in app folder

Create serializer.py and add 2 class(serializers) for models defined
Serializers will convert python object to JSON object, which is forwarded to front-end

---------------------------
for testing purpose, 
# Register your models in admin.py as below
admin.site.register(User)
admin.site.register(Activity)

but dont use this in production
---------------------------

run below command to creat admin(super user) since we need admin privileges to add/delete/change record details manually
< python manage.py createsuperuser >









