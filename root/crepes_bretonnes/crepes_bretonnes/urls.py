"""crepes_bretonnes URL Configuration

[...]
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # l'include vers blog/urls.py que l'on a mis dans les chapitres précédents
    path('blog/', include('blog.urls')),  
]
