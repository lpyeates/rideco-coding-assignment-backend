from django.urls import path
from .views import GroceryListCreateView, GroceryItemRetrieveUpdateDestroyView

urlpatterns = [
  path(
    '',
    GroceryListCreateView.as_view(),
    name='groceryitem-list-create'
  ),
  path(
    '<int:pk>',
    GroceryItemRetrieveUpdateDestroyView.as_view(),
    name='groceryitem-retrieve-update-destroy'
  ),
]