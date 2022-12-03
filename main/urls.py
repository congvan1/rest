from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import *

router = DefaultRouter(trailing_slash=False)
router.register(r'students', StudentView, basename='student')
router.register(r'teachers', TeacherView, basename='teacher')
router.register(r'classEngs', ClassEngView, basename='classEng')

urlpatterns = router.urls
