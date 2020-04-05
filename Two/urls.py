from django.conf.urls import url, include
from django.contrib import admin

from Two import views

urlpatterns = [
    url(r'^getperson/', views.get_person),
    url(r'^addperson/', views.add_person),
    url(r'^getpersons/', views.get_persons),
    url(r'^index/',views.index),
    url(r'^hello',views.HelloView.as_view()),
    url(r'^persons/$', views.PersonView.as_view()),
    url(r'^persons/(?P<id>\d+)', views.person1ApiView.as_view()),
    url(r'^blogs/$',views.BlogsAPIView.as_view()),
    url(r'^blogs/(?P<id>\d+)', views.BlogAPIView.as_view())

]