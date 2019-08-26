from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:pk>', views.checkout, name='checkout'),
]
