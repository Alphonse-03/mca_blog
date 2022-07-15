from django.urls import path,include
from . import views

urlpatterns = [
    path('comments',views.postComment,name="comment"),
    path('',views.blog,name="blog"),
    path('<str:slug>',views.blogpost,name="blogpost"),
   

]