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

### run migration 
```
# python manage.py makemigrations
# python manage.py migrate
```

### create django super user

### update static files
```
# python manage.py collectstatic
```

### test out
```
# python manage.py runserver
```


