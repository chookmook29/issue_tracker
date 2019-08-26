from django.urls import path
from . import views

urlpatterns = [
    path("delete/<ticket_id>", views.delete, name="delete"),
    path("show/<int:pk>", views.show, name="show_single"),
    path("show/<int:pk>/comment/", views.add_comment, name="add_comment"),
    path("add", views.add_ticket, name="add_ticket"),
    path("", views.all_tickets, name="home"),
    path("upvotes/", views.all_upvotes, name="upvotes"),
    path("commented/", views.all_commented, name="commented"),
    path("feature/", views.all_feature, name="feature"),
    path("bug/", views.all_bug, name="bug"),
]
