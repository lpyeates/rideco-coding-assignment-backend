from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import GroceryItem

class GroceryItemCreateTest(APITestCase):
  def test_create_groceryItem(self):
    data = {
      'name': 'bananas',
      'quantity': 2,
      'status': 'To Buy',
    }
    response = self.client.post('/groceries/', data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(GroceryItem.objects.count(), 1)
    self.assertEqual(GroceryItem.objects.get().name, 'bananas')
    self.assertEqual(GroceryItem.objects.get().quantity, 2)
    self.assertEqual(GroceryItem.objects.get().status, 'To Buy')

  def test_get_groceryItem(self):
    response = self.client.get('/groceries/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)