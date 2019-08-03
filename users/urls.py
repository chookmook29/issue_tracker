from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_user, name='logout'),
    path('change/', views.change_details, name='change'),
]
