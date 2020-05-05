from django.urls import path
from .views import CartItemAPIView

urlpatterns = [
    path('cartItem', CartItemAPIView.as_view())
]
