from django.urls import path

from first.views import index

urlpatterns = [
  path('', index)
]