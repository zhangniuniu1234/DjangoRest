from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from App import views
from App.views import BookViewSet

router=routers.DefaultRouter()
router.register("books",BookViewSet)
urlpatterns = [
    url(r'^index/',views.index),
]