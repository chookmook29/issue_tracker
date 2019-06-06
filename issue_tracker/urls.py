from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('ticket/', include('ticket.urls')),
    path('checkout/', include('checkout.urls')),
    path('login/', views.login_user, name='login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout/', views.logout_user, name='logout'),
    path('all_tickets/', views.all_tickets, name='all_tickets')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
