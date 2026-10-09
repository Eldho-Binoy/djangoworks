from django.shortcuts import render
from django.http import JsonResponse
from  django.views import View
from app.models import Student
# Create your views here.

class Studentdetails(View):
    def get(self,request):
        data={"studentname":"Amal","age":23,"course":"python","marks":56}
        return JsonResponse(data)

class Studentlist(View):
    def get(self,request):
        # data=[{"studentname":"Amal","age":23,"course":"python","marks":56},
        #       {"studentname":"Achu","age":22,"course":"django","marks":110},
        #       {"studentname":"Arun","age":21,"course":"datascience","marks":99}]
        queryset=Student.objects.all()
        data=list(Student.objects.all().values())
        # print(type(data))
        print(data)
        return JsonResponse(data,safe=False)