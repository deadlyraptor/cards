"""cards URL Configuration."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cards.apps.core.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
