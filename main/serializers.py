from rest_framework import serializers
from .models import Student, Teacher, ClassEng, UserAccount


class UserAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class UserStudentSerializers(serializers.ModelSerializer):
    student = StudentSerializers(read_only=True)
    class Meta:
        model = UserAccount
        fields = ['role','student']
        
class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class UserTeacherSerializers(serializers.ModelSerializer):
    teacher = TeacherSerializers(read_only=True)
    class Meta:
        model = UserAccount
        fields = ['role','teacher']
class ClassEngSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClassEng
        fields = '__all__'