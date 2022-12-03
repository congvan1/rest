from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import *
# Create your tests here.

class test_student(APITestCase):
    url = '/students/'
    
    def setUp(self):
        Student.objects.create(name='tuan', age=1, grade=1)
        
    def test_get_student(self):
        response = self.client.get(self.url)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['name'], 'tuan')
        
    def test_post_student(self):
        data = {
            "name": "tuan",
            "age": 16,
            "city": "HCM",
            "school_name": "DUT",
            "grade": 10,
        }
        response = self.client.post(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["name"], 'tuan')
        
    def test_update_student(self):
        pk = '1/'
        data = {
            "name": "tuan (updated)",
            "age": 16,
            "city": "HCM",
            "school_name": "DUT",
            "grade": 10,
        }
        response = self.client.patch(self.url + pk, data=data)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["name"], 'tuan (updated)')
        
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
        Teacher.objects.create(name='GV Hoa', age=1)
        
    def test_get_teacher(self):
        response = self.client.get(self.url_teacher)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['name'], 'GV Hoa')
       
    def test_post_teacher(self):
        data = {
            "name": "giao vien A",
            "age": 33,
            "address": "HA NOI",
            "phone": "0905123456",
            "license": "toiec",
        }
        response = self.client.post(self.url_teacher, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["name"], 'giao vien A')
        
    def test_update_teacher(self):
        pk = '1/'
        data = {
            "name": "giao vien A (updated)",
            "age": 33,
            "address": "HA NOI",
            "phone": "0905123456",
            "license": "toiec",
        }
        response = self.client.patch(self.url_teacher + pk, data=data)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["name"], 'giao vien A (updated)')
        
    def test_delete_teacher(self):
        pk = '1/'

        response_delete = self.client.delete(self.url_teacher + pk)
        response_get = self.client.get(self.url_teacher + pk)
        
        self.assertEqual(response_delete.status_code, 204)
        self.assertEqual(response_get.status_code, 404)


class test_class_english(APITestCase):
    url_class_english = '/classEngs/'
    def setUp(self):
        ClassEng.objects.create(level=450, description='lớp học toiec cho người mới, target 450 điểm')
        
    def test_get_class_english(self):
        response = self.client.get(self.url_class_english)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['description'], 'lớp học toiec cho người mới, target 450 điểm')
       
    def test_post_class_english(self):
        data = {
            "level": 450,
            "description": "lớp học toiec cho người mới, target 450 điểm",
            "fee": "1300000",
        }
        response = self.client.post(self.url_class_english, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["level"], 450)
        
    def test_update_class_english(self):
        pk = '1/'
        data = {
            "level": 700,
        }
        response = self.client.patch(self.url_class_english + pk, data=data)
        result = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["level"], 700)
        
    def test_delete_class_english(self):
        pk = '1/'

        response_delete = self.client.delete(self.url_class_english + pk)
        response_get = self.client.get(self.url_class_english + pk)
        
        self.assertEqual(response_delete.status_code, 204)
        self.assertEqual(response_get.status_code, 404)
