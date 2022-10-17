# Getting started
## Open your cmd, then clone the project
```
cd *your_directory*
git clone https://github.com/DJsega1/django-intensive.git
cd django-intensive
```  
## Create an virtual environment
___
**Windows**
```
python -m venv venv
```
**Linux/Mac**
```
python3 -m venv venv
```
  
## Activate virtual enviroment
___
**Windows**
```
venv\Scripts\activate
```
**Linux/Mac**
```
source venv/bin/activate
```

## Install the project dependencies
___
**Windows**
```
pip install -r requirements.txt
```
**Linux/Mac**
```
pip3 install -r requirements.txt
```
## Create .env file 
___
**Create .env file in the project directory (path should be "django-intensive/.env")**  
**Write in it the following variables (if you want to add some hosts, separate it by whitespace):**
```
SECRET_KEY = '{your_secret_key}'
DEBUG = *True or False*
ALLOWED_HOSTS = '{host1} {host2}'
```
## Start the development server
___
```
cd intensive
python manage.py runserver
```  
___
The project starts on **127.0.0.1:8000** by default.  
If you want to change that, read the docs:  
https://docs.djangoproject.com/en/3.2/ref/django-admin/#runserver  
**Press Ctrl+C in order to stop the server.**
