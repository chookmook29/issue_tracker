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
    path('', include('users.urls')),
    # Only for development and debug, user-uploaded media files from MEDIA_ROOT
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
