from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
# demo/api/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import User
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.save_url = reverse('save')
        self.update_url = reverse('update')
        self.login_url = reverse('login')
        self.list_url = reverse('list')
        self.info_url = reverse('info')

        self.test_user = User.objects.create(
            username='test',
            name='Test User',
            password='password',
            role=1,
            status='active',
            reserve1='reserve1',
            reserve2='reserve2',
            reserve3='reserve3',
            reserve4='reserve4',
            reserve5='reserve5',
            create_time='2023-01-01 00:00:00'
        )

    def test_save_user(self):
        data = {
            'username': 'test2',
            'name': 'Test User2',
            'password': 'password2',
            'role': 2,
            'status': 'active',
            'reserve1': 'reserve12',
            'reserve2': 'reserve22',
            'reserve3': 'reserve32',
            'reserve4': 'reserve42',
            'reserve5': 'reserve52'
        }
        response = self.client.post(self.save_url, json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.count(), 2)

    def test_update_user(self):
        data = {
            'id': self.test_user.id,
            'username': 'updated',
        }
        response = self.client.post(self.update_url, json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.get(id=self.test_user.id).username, 'updated')

    def test_login(self):
        data = {
            'username': 'test',
            'password': 'password',
        }
        response = self.client.post(self.login_url, json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(json.loads(response.content)['success'])

    def test_list_users(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(json.loads(response.content)['data']), 1)

    def test_info(self):
        response = self.client.get(self.info_url, {'id': self.test_user.id})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json.loads(response.content)['data']['username'], 'test')
