# Blogger_Website:
This is a simple Django 2.2 project using template with preferred setup.
Also Used Docker compose to Dockerize Django App.


# Introduction:
Django is an free and open source web application framework written in Python. A framework is nothing more than a collection of modules that make development easier. They are grouped together, and allow you to create applications or websites from an existing source, instead of from scratch.


# Pre-configurations needed:
You will require Python and django in your system. 
To download follow the link:
For Python: https://www.python.org/downloads/
For Django: ``` $ pip install Django==3.0.5``` should be used.
 
# Perform Database Migration:

```
$ python manage.py check
$ python manage.py migrate 
   ```
   
# Deployment:
 
This project assumes you have an Docker installed in system.
If not Download Docker First, to download follow the link: https://www.docker.com/products/docker-desktop


# Commands To :

## Run Development Server:-
`$ docker-compose up -d`
 
## To Stop The Server:
 `$ docker-compose down`  
 

# Output will be Avaiable on : 

``` localhost:8000/ ```
