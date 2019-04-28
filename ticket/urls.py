from django.urls import path
from . import views

urlpatterns = [
    path('', views.tickets, name='ticket'),
    path('delete/<ticket_id>', views.delete, name='delete'),
    path('show/<ticket_id>', views.show, name='show_single'),
]
