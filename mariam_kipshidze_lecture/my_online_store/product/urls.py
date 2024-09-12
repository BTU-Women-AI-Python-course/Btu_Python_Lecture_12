from django.urls import path

from product.views import example_view

urlpatterns = [
    path('example_view/', example_view, name='example_view'),
]
