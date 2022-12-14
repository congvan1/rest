from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import *
# Create your tests here.
class test_account(APITestCase):
    url = '/accounts/'
    
    def setUp(self):
        UserAccount.objects.create(username='van', password='123')
        
    def test_get_account(self):
        response = self.client.get(self.url)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['username'], 'van')
        
    def test_post_account(self):
        data = {
            "username": "nhan",
            "password": "123",
            "role": "STUDENT"
        }
        response = self.client.post(self.url, data=data)
        result = response.json()
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["username"], 'nhan')
        
    def test_update_account(self):
        pk = '1/'
        data = {
            "username": "nhan (updated)",
            "password": "123",
            "role": "STUDENT"
        }
        response = self.client.patch(self.url + pk, data=data)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["username"], 'nhan (updated)')
    
    def test_delete_account(self):
        pk = '1/'

        response_delete = self.client.delete(self.url + pk)
        response_get = self.client.get(self.url + pk)
        result = response_get.json()
        
        self.assertEqual(response_delete.status_code, 204)
        self.assertEqual(response_get.status_code, 404)
class test_student(APITestCase):
    url = '/students/'
    
    def setUp(self):
        user = UserAccount.objects.create(username='van', password='123')
        user2 = UserAccount.objects.create(username='van1', password='123')

        student = Student.objects.create(id_user=user, name='tuan', age=1, grade=12)
        
    def test_get_student(self):
        response = self.client.get(self.url)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['name'], 'tuan')
        
    def test_post_student(self):

        data = {
            "name": "Thanh Nhân",
            "age": 21,
            "city": "Da Nang",
            "school_name": "Hoa Vang",
            "grade": 12,
            'id_user': 2
        }
        response = self.client.post(self.url, data=data)
        result = response.json()
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["name"], 'Thanh Nhân')
        
    def test_update_student(self):
        pk = '1/'
        data = {
            "name": "Thanh Nhân (updated)",
            "age": 21,
            "city": "Da Nang",
            "school_name": "Hoa Vang",
            "grade": 12,
            'id_user': 2
        }
        response = self.client.patch(self.url + pk, data=data)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["name"], 'Thanh Nhân (updated)')
        
    def test_delete_student(self):
        pk = '1/'

        response_delete = self.client.delete(self.url + pk)
        response_get = self.client.get(self.url + pk)
        result = response_get.json()
        
        self.assertEqual(response_delete.status_code, 204)
        self.assertEqual(response_get.status_code, 404)
        
        
class test_teacher(APITestCase):
    url_teacher = '/teachers/'
    def setUp(self):
        user1 = UserAccount.objects.create(username='van', password='123')
        Teacher.objects.create(id_user=user1, name='GV Hoa', age=1)
        
    def test_get_teacher(self):
        response = self.client.get(self.url_teacher)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['name'], 'GV Hoa')

class test_(APITestCase):
    url = '/rates/'
    def setUp(self):
        user1 = UserAccount.objects.create(username='van', password='123')
        student = Student.objects.create(id_user=user1, name='GV Hoa', age=1, grade=12)
        
        user2 = UserAccount.objects.create(username='van2', password='123')
        teacher = Teacher.objects.create(id_user=user2, name='GV Hoa 222', age=1)
        
        Rate.objects.create(id_student=student, id_teacher=teacher, chuyen_mon=1)
        
        user3 = UserAccount.objects.create(username='van32', password='123')
        Student.objects.create(id_user=user3, name='GV Hoa', age=1, grade=12)
        
        user4 = UserAccount.objects.create(username='van23', password='123')
        teacher = Teacher.objects.create(id_user=user4, name='GV Hoa 222', age=1)
        
    def test_get_rate(self):
        response = self.client.get(self.url)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['chuyen_mon'], 1)
        
    def test_post_rate(self):
        data = {
            "trinh_do_su_pham": 2,
            "chuyen_mon": 2,
            "su_yeu_thich": 2,
            "id_student": 2,
            "id_teacher": 2
        }
        response = self.client.post(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["chuyen_mon"], 2)
        
        
    def test_update_rate(self):
        pk = '1/'
        data = {
            "trinh_do_su_pham": 2,
            "chuyen_mon": 3,
            "su_yeu_thich": 2,
            "id_student": 2,
            "id_teacher": 2
        }
        response = self.client.patch(self.url + pk, data=data)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["chuyen_mon"], 3)
        
    def test_delete_rate(self):
        pk = '1/'

        response_delete = self.client.delete(self.url + pk)
        response_get = self.client.get(self.url + pk)
        
        self.assertEqual(response_delete.status_code, 204)
        self.assertEqual(response_get.status_code, 404)
