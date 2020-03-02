from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name ='home'),
    path('a/', views.home1 , name ='home1'),
    path('b/', views.homepost , name ='homepost'),
    path('a/add/', views.add , name ='add'),
    path('b/add', views.addb , name ='add'),
]
