from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main import views

router = DefaultRouter()
router.register(r'students', views.StudentView, basename='student')
router.register(r'teachers', views.StudentView, basename='teacher')
router.register(r'classEngs', views.StudentView, basename='classEng')

urlpatterns = [
    path('', include(router.urls))
]
