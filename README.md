# Real Estate Project - Lalpurja.com
This is a simple django project with minimal features which is easy to follow on. 
Admin of the site publishes property listings and associate a realtors for each listing.
Customer can now access those listings based on their preferences and make an inquiry. To make an inquiry, one need not be signed in but if they do, the inquiry populates their data automatically during inquiry.
Register page will signup for an account.

Note: Once inquired about any property, this will trigger an email to the realtor but this functionality is not working - try out yourself and do leave a comment if anyone succeeded to do so.

# project setup 
## just for reference how this project was created.

# Git clone this project.
```
# git clone <URL>
# cd realestate_project
```

### setup venv
```
# python3 -m venv ./venv
# source venv/bin/activate
```

### setup python modules
```
# pip install -r requirements.txt
```

### setup postgres server locally and create database/dbuser
```
for MAC: https://postgresapp.com/
for WIN: https://www.postgresql.org/download/windows/

Open postgres and this brings a psql terminal
postgres=# \password postgres
Enter password
postgres=# CREATE DATABASE btredb OWNER postgres; 
```

### Install pgadmin for postgres adminsitation GUI
```
pgadmin.org
```

### update db/password in lalpurja/settings.py
```
Note: If you choose to use sqlite3 databse, update settings.py with correct driver as shown below.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### run migration 
```
# python manage.py makemigrations
# python manage.py migrate
```

### create django super user

### update static files
```
# python manage.py collectstatic

Note: Still backgroung image to index page is not rendered. Fix on your own and leave a comment if anyone found a fix.
```

### test out
```
# python manage.py runserver

Note: Update some properties/realtors data through admin page.
```


