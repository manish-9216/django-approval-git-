from django import views
from django.urls import path  
from . import views


urlpatterns = [  
    path('', views.signup,name = 'signup'),  
    path('login',views.login,name='login'),  
    path('activate/<slug:uidb64>/<slug:token>/',views.activate, name='activate'),  
]  