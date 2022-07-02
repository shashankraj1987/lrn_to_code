# Django notess for Reference

_______________________________________________________________~

Django Terms.

1. wsgi file -- Web Server Gateway Interface. This is the
    actual server that renders HTTP Request.
2. manage.py -- This is where we execute our commands from.
3. sqlite -- The default database with Django.
4. url.py -- This is where all the routing and links are present.
5. asgi.py -- Django's support for asynchronous calls

6.

Create a Python Boilerplate file.

~~~python
    django-admin startproject studybud

~~~

Run Django Server.

~~~python
    python3 manage.py runserver

~~~

Create a Python App.

~~~python
    python3 manage.py startapp base
    '''
    This Generates a folder called base. However, this needs to be added to the config files. 
    So that django could know the existance of this file. 
    It's Entry needs to be present in the INSTALLED_APPS section of Settings.py
    We need to point to the BaseConfig class of apps.py from the created app in the INSTALLED_APPS list.
    '''

~~~

_______________________________________________________________
