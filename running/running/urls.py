from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from application.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    url('', include('social_django.urls', namespace='social')),
    path('auth/', include('application.urls')),
]
