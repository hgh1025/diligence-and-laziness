from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='main_index'),
    path('home', views.home, name='main_home'),
    path('commute', views.commute, name='main_commute'),
    path('join', views.join, name= 'main_join'),
    path('mypage', views.mypage , name='main_mypage'),
    path('schedules', views.schedules , name='main_schedules'),
    path('calendar', views.calendar , name='main_calendar'),
    path('login', views.login, name='main_login'),
    path('logout', views.logout , name='main_logout'),
] 