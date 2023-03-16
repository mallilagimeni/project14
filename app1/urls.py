from django.urls import path
from app1.views import *


app_name='app1'

urlpatterns=[
    path('app1_first/',app1_first,name='app1_first'),
    path('app1_sec/',app1_sec,name='app1_sec'),
]