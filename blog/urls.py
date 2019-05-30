from django.urls import path
from . import views

urlpatterns = [
   path('', views.blogs, name='blogs'),
   path('show/<int:pk>', views.single_blog, name='single_blog'),
]
