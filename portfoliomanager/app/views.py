from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
# Create your views here.

class About(View):
    def get(self,request):
        data={"id":1,
              "name":"Arun Vevu",
              "title":"title",
              "DOB":"2004-08-17",
              "email":"arun@gmail.com",
              "contact":"9878767656",
              "location":"kochi",
              "GitHubURL":"arungithub",
              "LinkdInURl":"arunlinkdin"}
        return JsonResponse(data)

class Education(View):
    def get(self,request):
        data={"id":1,
              "institution":"AISAT",
              "course":"Python",
              "university":"KTU",
              "startyear":"2022",
              "endyear":"2026",
              "grade":"A+",
              "description":"Very good boy"}
        return JsonResponse(data)

class Projects(View):
    def get(self,request):
        data=[
            {"id":1,
             "projectname":"fishtank",
             "description":"sooper fishtank",
             "technologies":"python, java",
             "duration":"8 months",
             "liveURL":"ww.thisistheurl.com"},
            {"id": 2,
             "projectname": "tigercage",
             "description": "sooper cage",
             "technologies": "python, react",
             "duration": "20 months",
             "liveURL": "ww.thisistheonlyurl.com"}
        ]
        return JsonResponse(data,safe=False)