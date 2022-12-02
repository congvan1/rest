from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Teacher, ClassEng
from .serializers import StudentSerializers, TeacherSerializers, ClassEngSerializers

# Create your views here.
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
    
class ClassEngView(viewsets.ModelViewSet):
    queryset = ClassEng.objects.all()
    serializer_class = ClassEngSerializers