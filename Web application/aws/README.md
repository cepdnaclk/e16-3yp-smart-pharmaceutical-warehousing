

# MEDshop

This is a e-commerce website built with Django.
---
### web site

[www.medishop.com](http://ec2-34-228-244-128.compute-1.amazonaws.com:8000/)

aws server is not working for 24h 

---
## Quick demo

![alt text]( https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/Web%20application/aws/doc/demo.gif "Logo")

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
![alt text]( https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/Web%20application/aws/doc/login.gif )

```
sign up
```

![alt text]( https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/Web%20application/aws/doc/signup.png )

### checkout


![alt text]( https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/Web%20application/aws/doc/checkout.png )


### mqtt message (order)
fernet encryption
![alt text]( https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/Web%20application/aws/doc/mqtt.png )

### change item details

![alt text]( https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/Web%20application/aws/doc/change.gif)
