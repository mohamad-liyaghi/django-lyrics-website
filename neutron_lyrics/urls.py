from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#--------------------------------Urls---------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("lyrics.urls")),
    path('api/',include("api.urls")),
]
urlpatterns += staticfiles_urlpatterns()
#---------------------------------------------------------------------
