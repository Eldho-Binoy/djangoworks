from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

# def First(request):
#     if (request.method=="GET"):
#         return HttpResponse("First")
#
# def Second(request):
#     if(request.method=="GET"):
#         return HttpResponse("Second")

class First(View):
    def get(self,request):
        return HttpResponse("First page")

class Second(View):
    def get(self,request):
        return HttpResponse("Second page")