from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=50, null=False, unique = True)
    password = models.CharField(max_length=50, null=False)
    r = [('STUDENT','Học sinh'),('TEACHER','Gia sư')]
    role = models.CharField(max_length=10, null=False, choices=r, default='STUDENT')

class Student(models.Model):
    id_user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='student', null=False)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=200)
    school_name = models.CharField(max_length=100)
    grade = models.IntegerField()

class Teacher(models.Model):
    id_user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    licenses = models.CharField(max_length=100, default='None')
    image_license = models.ImageField(upload_to='images', null=True, default=None)
    avatar = models.ImageField(upload_to='images', null=True, default=None)
    describe_detail = models.CharField(max_length=1000, null=False, default="Chào bạn tôi là gia sư tiếng anh")

class Rate(models.Model):
    id_student = models.OneToOneField(Student,on_delete=models.CASCADE)
    id_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    trinh_do_su_pham = models.IntegerField(default=2) # 2.5
    chuyen_mon = models.IntegerField(default=2)  #    1.5
    su_yeu_thich = models.IntegerField(default=2) #  1
