from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *


app_name= 'core'

urlpatterns=[
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('userregister/',userreg.as_view(),name='register'),
    path('userlogin/',userlogin.as_view(),name='login'),
    
]