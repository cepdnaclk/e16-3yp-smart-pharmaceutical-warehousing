<p align="center">
  <p align="center">
    <a href="https://justdjango.com/?utm_source=github&utm_medium=logo" target="_blank">
      <img src="https://assets.justdjango.com/static/branding/logo.svg" alt="JustDjango" height="72">
    </a>
  </p>
  <p align="center">
    Medshop.
  </p>
</p>


# MEDshop

This is a e-commerce website built with Django.

## Quick demo

[![alt text](https://https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/tree/main/Web%20application/aws/doc/demo.gif "Logo")]

---

## Running this project

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

