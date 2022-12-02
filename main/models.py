from django.db import models
from django.contrib.auth.models import User
        
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student', null=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=200)
    school_name = models.CharField(max_length=100)
    grade = models.IntegerField()

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    license = models.CharField(max_length=100)
    image_license = models.ImageField(upload_to='images', null=False, default=None)
    avatar = models.ImageField(upload_to='images', null=False, default=None)

class ClassEng(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    level = models.IntegerField()
    description = models.CharField(max_length=1000)
    fee = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)