from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main import views

router = DefaultRouter()
router.register(r'accounts', views.UserAccountView, basename='account')
router.register(r'students', views.StudentView, basename='student')
router.register(r'teachers', views.TeacherView, basename='teacher')
router.register(r'rates', views.RateView, basename='rate')
router.register(r'informationClass', views.InfortionClassView, basename='information_class')


urlpatterns = [
    path('', include(router.urls))
]
