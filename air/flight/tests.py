# demo/api/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Flight
import json

class FlightTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.flight = Flight.objects.create(
            airCode="Test Aircode",
            status="Active",
            comCode="Test ComCode",
            flag="Test Flag",
            fliAaddress="Test AAddress",
            fliAtime="Test ATime",
            fliBaddress="Test BAddress",
            fliBtime="Test BTime",
            fliCfare="Test CFare",
            fliCnumber="Test CNumber",
            fliDiscount="Test Discount",
            fliFfare="Test FFare",
            fliFnumber="Test FNumber",
            fliNo="Test FliNo",
            fliRefundtime="Test Refundtime",
            fliYfare="Test YFare",
            fliYnumber="Test YNumber",
            # The other fields are left blank for simplicity.
        )

    def test_save_flight(self):
        url = reverse('save')  # replace 'save_flight' with the actual name of the url
        data = {
            "airCode": "New Aircode",
            "status": "Active",
            # Similarly add other fields.
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

    def test_update_flight(self):
        url = reverse('update')  # replace 'update_flight' with the actual name of the url
        data = {
            "id": self.flight.id,
            "status": "Inactive",
            # Similarly add other fields that you want to update.
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

    def test_list_flights(self):
        url = reverse('list')  # replace 'list_flights' with the actual name of the url
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

    def test_page_flights(self):
        url = reverse('page')  # replace 'page_flights' with the actual name of the url
        data = {
            "pageNum": 1,
            "pageSize": 10
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)
