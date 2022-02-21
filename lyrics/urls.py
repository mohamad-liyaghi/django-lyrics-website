from django.urls import path
from .views import *
#--------------------------------Urls---------------------------------
urlpatterns = [
    path("",lyrics,name="home"),
    path("result/",result,name="result"),
]
#----------------------------------------------------------------------
