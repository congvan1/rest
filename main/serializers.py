from rest_framework import serializers
from .models import Student, Teacher, ClassEng

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class ClassEngSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClassEng
        fields = '__all__'