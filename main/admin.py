from django.contrib import admin
from django.contrib.auth.models import User
from .models import Student, Teacher, ClassEng

# Register your models here.
admin.register(User)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(ClassEng)