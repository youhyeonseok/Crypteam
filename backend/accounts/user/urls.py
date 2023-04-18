from django.urls import path, include
from .views import *

urlpatterns =[
    path('userinfo/', UserInfo, name = 'api-register'),
]