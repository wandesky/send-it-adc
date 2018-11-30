import unittest
from app import app
import json

class TestParcel(unittest.TestCase):
    '''Tests fetching of all parcel delivery orders'''
    def test_get_parcels(self):
        self.response = app.test_client().get('/api/v1/parcels')
        self.assertEqual(self.response.status_code, 200)