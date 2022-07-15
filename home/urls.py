from django.urls import path,include
from . import views

urlpatterns = [
    path('about',views.about,name="about"),
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('search',views.search,name="search"),
    path('loginhandle',views.loginhandle,name="loginhandle"),
    path('logouthandle',views.logouthandle,name="logouthandle"),
    path('registerhandle',views.registerhandle,name="registerhandle"),
  
]