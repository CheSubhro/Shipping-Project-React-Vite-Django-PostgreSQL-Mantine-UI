
from django.urls import path
from .views import CalculateShippingView

urlpatterns = [
    path('calculate/', CalculateShippingView.as_view(), name='calculate-shipping'),
]