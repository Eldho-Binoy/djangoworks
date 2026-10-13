from django.shortcuts import render
from django.http import JsonResponse
from  django.views import View
from app.models import Movie

# Create your views here.

class Movielist(View):
    def get(self,request):
        data=list(Movie.objects.all().values())
        return JsonResponse(data,safe=False)