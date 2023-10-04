from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from feed import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("",views.index,name=""),
    path("second/",views.second_page,name="second"),
    path("seconds/",views.second_pages,name="seconds"),

]