# Neutron lyrics
## General info
Simple website using <a href="https://www.djangoproject.com/">Django</a> , <a href="https://www.django-rest-framework.org/">Drf</a> and <a href= "https://github.com/johnwmillr/LyricsGenius" >lyrics genius</a>
</br>
This project is unfinished, feel free to edit it !
## Setup
Before using , you'll need to sign up for an account that authorizes access to <a href="https://genius.com/signup_or_login">the Genius API.</a> The Genius account provides a ```access_token``` that is required by the project.
<br/>Insert your token, in this <a href= "https://github.com/Ml06py/neutron-lyrics/blob/master/extensions/token.py">token</a> field.
## Requirment
```
$ pip install django
$ pip install djangorestframework
$ pip install django-crispy-forms
$ pip install lyricsgenius
```
## Usage
```
$ git clone https://github.com/mohamad-liyaghi/django-lyrics-website.git
$ cd django-lyrics-website
$ python manage.py migrate
$ python manage.py runserver
```
## Using Api
```
$ import requests
$ print(requests.get("http://127.0.0.1:8000/api/lyrics/derakht/ebi").text)
```
