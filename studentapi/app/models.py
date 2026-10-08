from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    course=models.CharField(max_length=20)
    marks=models.IntegerField()

class Course(models.Model):
    mode_choice=(("offline","OFFLINE"),("online","ONLINE"))
    course_name=models.CharField(max_length=30)
    instructor=models.CharField(max_length=20)
    fee=models.IntegerField()
    duration=models.CharField(max_length=20)
    mode=models.CharField(max_length=20, choices=mode_choice)