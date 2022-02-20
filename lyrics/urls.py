from django.urls import path
from .views import *
urlpatterns = [
    path("",lyrics,name="home"),
    path("result/",result,name="result"),
]