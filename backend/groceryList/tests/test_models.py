from django.test import TestCase

from ..models import GroceryItem

class GroceryItemModelTest(TestCase):
  @classmethod
  def setUpTestData(self):
    self.object = GroceryItem.objects.create(name='bananas', quantity=2, status='To Buy')

  def test_object_name(self):
    item = GroceryItem.objects.get(id=1);
    self.assertEqual(str(self.object), item.name)
