from django.db import models

# Create your models here.

class GroceryItem(models.Model):
  name = models.CharField(max_length=200)
  quantity = models.IntegerField()
  status = models.CharField(max_length=200, default='To Buy')

  def __str__(self):
    return self.name
