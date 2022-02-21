from django.urls import path
from .views import lyrics,home
urlpatterns = [
    path('',home),
    path('lyrics/<str:song_name>/<str:artist_name>/',lyrics)
]