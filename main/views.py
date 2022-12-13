from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student, Teacher, Rate, UserAccount, InformationClass
from .serializers import StudentSerializers, TeacherSerializers, RateSerializers, UserAccountSerializers, UserStudentSerializers, UserTeacherSerializers, InformationClassSerializers

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']
    def create(self, request, *args, **kwargs):
        data = request.data
        serializers = TeacherSerializers(data=data)
        try:
            if serializers.is_valid(raise_exception=True):
                teacher = serializers.save()
                Rate.objects.create(teacher=teacher)
                return Response(data="Teacher created",status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)           

    @action(detail=True,methods=['GET'])
    def GetRate(self,request,pk):
        try:
            teacher = Teacher.objects.filter(id=pk)
            rating = Rate.objects.filter(id_teacher=teacher[0].id)
            serializer = RateSerializers(rating,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error :":str(e)},status=status.HTTP_404_NOT_FOUND)
    @action(detail=True,methods=["Get"])
    def GetClass(self,request,pk):
        try:
            teacher = Teacher.objects.filter(id=pk)
            classes = Rate.objects.filter(id_teacher=teacher[0].id)
            serializer = InformationClassSerializers(classes,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error :":str(e)},status=status.HTTP_404_NOT_FOUND)

    
class RateView(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializers
    
class InfortionClassView(viewsets.ModelViewSet):
    queryset = InformationClass.objects.all()
    serializer_class = InformationClassSerializers