

# Operator Interface

This is a graphical user interface built for the warehouse operator using tkinter.
---
### web site


---
## Quick demo

![alt text]( )

---

# Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pipenv shell
```
Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```
Now you can run the project with this command (gunicorn)

```
gunicorn djecommerce.wsgi:application --bind 0.0.0.0:8000
```
---

# Functions

### password authentication
```
login
```
```
sign up
```

### checkout

### mqtt message (order)

### change item details


