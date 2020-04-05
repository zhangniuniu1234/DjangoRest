
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException,NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Two.models import Person, Blog
from Two.serializers import PersonSerializers, BlogSerializers


def get_person(request):
    person=Person.objects.first()
    serializer=PersonSerializers(person)
    print(serializer.data)
    print(type(serializer.data))
    data={
        "msg":"OK",
        "status":200,
        "data":serializer.data
    }
    return JsonResponse(data)

def add_person(request):
    p_name=request.POST.get("p_name")
    p_age=request.POST.get("p_age")
    # person=Person()
    # person.p_name=p_name
    # person.p_age=p_age
    # person.save()
    # serializer=PersonSerializers(person)
    # data = {
    #     "msg": "OK",
    #     "status": 201,
    #     "data": serializer.data
    # }

    person_data={
        "p_name":p_name,
        "p_age":p_age
    }
    serializer = PersonSerializers(data=person_data)

    if not serializer.is_valid():
            return JsonResponse(serializer.errors)

    serializer.save()
    return JsonResponse(serializer.data)

def get_persons(request):
    persons=Person.objects.all()
    serializer = PersonSerializers(persons,many=True)
    data = {
        "msg": "OK",
        "status": status.HTTP_201_CREATED,
        "data": serializer.data
    }
    return JsonResponse(data)

@api_view(['GET','POST'])
def index(request):
    print(type(request))
    return HttpResponse("hello")

class HelloView(APIView):
    def get(self,request):
        data={
            "msg":"ok"
        }
        raise APIException(detail="不想写了")
class PersonView(APIView):
    def get(self,request):
        persons=Person.objects.all()
        serializer=PersonSerializers(persons,many=True)
        return Response(serializer.data)
    def post(self,request):
        p_name=request.data.get("p_name")
        p_age=request.data.get("p_age")
        person_info={
            "p_name":p_name,
            "p_age":p_age
        }
        serialiazer=PersonSerializers(data=person_info)
        if not serialiazer.is_valid():
            return Response(serialiazer.errors)
        serialiazer.save()
        return Response(serialiazer.data)

class person1ApiView(APIView):

    def get_object(self,id):
        try:
            person = Person.objects.get(pk=id)
            return person
        except Exception as e:
            raise NotFound()

    def get(self,request,id):
        serialiazer=PersonSerializers(self.get_object(id))
        return Response(serialiazer.data)
    def delete(self,request,id):
        person=self.get_object(id)
        person.delete()
        return Response("删除成功")

class BlogsAPIView(GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    def get(self,request):
        queryset=self.get_queryset()
        serializer=self.get_serializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class BlogAPIView(GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers






