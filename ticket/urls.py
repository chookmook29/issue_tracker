from django.urls import path
from . import views

urlpatterns = [
	path('', views.tickets, name='ticket'),
	path('delete/<ticket_id>', views.delete, name='delete'),
]
