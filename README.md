## General Idea
This small project is Django web site which help to list shops and also provide to the user the ability to like or 
dislike shops, the user can create an account using email address, a user can list his favorite shops and remove them 
from this list, the user can also dislike shops those shops will disappear for two hours.

##How To Use
Fist of all we need to install requirements:
```
pip3 install -r requirements.txt
```
Then create tables:
```
./manage.py migrate
```
Then create a user:
```
./manage.py createsuperuser
```
after that you can enter your email and password

Run the server 
```
./manage.py runserver
```
then go to the admin page ```127.0.0.1:8000/admin``` and enter your credentials , then you can add shops 

other user don't have rights to do that, a normal user can connect to ```127.0.0.1:8000/shops```, if he isn't authenticated 
a login page will appear, he can also create a new account in this page .