from App.models import Book
from rest_framework import serializers

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Book
        fields=("url","b_name","b_price")