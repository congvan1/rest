from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Teacher, ClassEng, UserAccount
from .serializers import StudentSerializers, TeacherSerializers, ClassEngSerializers, UserAccountSerializers, UserStudentSerializers, UserTeacherSerializers

# Create your views here.
class UserAccountView(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializers
    @action(detail=False, methods = ['get'])
    def getUser(self,request):
        try:
            param = request.query_params
            user = UserAccount.objects.get(username__exact=param.get('username'),password__exact=param.get('password'))
            if user.role == 'STUDENT':
                serializer = UserStudentSerializers(user)
            elif user.role == 'TEACHER':
                serializer = UserTeacherSerializers(user)
            return Response(serializer.data)
        except:
            return Response(data="Account does not exsit",status=status.HTTP_404_NOT_FOUND)

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
    
class ClassEngView(viewsets.ModelViewSet):
    queryset = ClassEng.objects.all()
    serializer_class = ClassEngSerializers