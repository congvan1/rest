from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=50, null=False, unique = True)
    password = models.CharField(max_length=50, null=False)
    r = [('STUDENT','Học sinh'),('TEACHER','Gia sư')]
    role = models.CharField(max_length=10, null=False, choices=r, default='STUDENT')

class Student(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='student', null=False,primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=200)
    school_name = models.CharField(max_length=100)
    grade = models.IntegerField()

class Teacher(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    licenses = models.CharField(max_length=100, default='None')
    image_license = models.ImageField(upload_to='images', null=True, default=None)
    avatar = models.ImageField(upload_to='images', null=True, default=None)

class ClassEng(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    level = models.IntegerField()
    description = models.CharField(max_length=1000)
    fee = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)