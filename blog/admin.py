from django.contrib import admin

from .models import Blog, Blog_comment

admin.site.register(Blog)
admin.site.register(Blog_comment)
