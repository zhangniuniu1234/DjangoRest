from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from App.models import Book
from App.serializers import BookSerializer

def index(request):
    return HttpResponse("hello index")

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer