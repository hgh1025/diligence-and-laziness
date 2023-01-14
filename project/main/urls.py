from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='main_index'),
    path('join', views.join, name= 'main_join'),
    path('mypage', views.mypage , name='main_mypage'),
    path('calendar', views.calendar , name='main_calendar'),
    path('logout', views.logout , name='main_logout'),
]