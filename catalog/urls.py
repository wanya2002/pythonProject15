from django.urls import path
from catalog.apps import CatalogConfig

app_name = CatalogConfig.__name__

from catalog.views import index, contact

urlpatterns = [
  path('', index),
  path('contacts/', contact)
]