from django.test import TestCase, Client
from django.urls import reverse
from .models import Air
import json

class AirTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.air1 = Air.objects.create(
            airCode="AC100",
            airCna="Test CNA",
            status="Active",
            #Add all your other fields here
        )

    def test_delete(self):
        response = self.client.get(reverse('delete'), {'id': self.air1.id})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Air.objects.filter(id=self.air1.id).exists())

    def test_update(self):
        update_data = {
            'id': self.air1.id,
            'airCode': 'AC200',
            #Add all your other fields here
        }
        response = self.client.post(reverse('update'), json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.air1.refresh_from_db()
        self.assertEqual(self.air1.airCode, 'AC200')

    def test_page(self):
        response = self.client.post(reverse('page'), json.dumps({'pageNum': 1, 'pageSize': 5}), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_save(self):
        save_data = {
            'airCode': 'AC300',
            'airCna': 'Test CNA 2',
            'status': 'Inactive',
            #Add all your other fields here
        }
        response = self.client.post(reverse('save'), json.dumps(save_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Air.objects.filter(airCode='AC300').exists())
