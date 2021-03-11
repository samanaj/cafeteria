from django.urls import path, include

from . import views


urlpatterns = [
    #home
    path('', include('rest_auth.urls')),
   
]

