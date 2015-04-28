from django.conf.urls import patterns, include, url
from django.contrib import admin
from lend import views

urlpatterns = patterns('',
    url(r'^$', views.dasboard, name="dashboard"),
    url(r'^addbook/', views.addbook, name="add_book"),
    url(r'^lendbook/', views.lend, name="lend_book"),
    url(r'^alldetails/', views.details, name="details")
)

