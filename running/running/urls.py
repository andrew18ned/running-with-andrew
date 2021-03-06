from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authViews
from application.views import index, about, contact, profile, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    url('', include('social_django.urls', namespace='social')),
    path('auth/', include('application.urls')),
    path('about/', about),
    path('contact/', contact),
    path('accounts/profile/', profile, name='profile'),
    path('logout/', authViews.LogoutView.as_view(next_page='/'), name='logout'),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, 
                                        document_root = settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, 
                                        document_root=settings.STATIC_ROOT)