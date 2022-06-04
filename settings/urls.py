"""
demo_curd URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView
from apps.users.views import logoutview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.users.urls', 'users'))),
    path('login/', LoginView.as_view(
        template_name='users/login_page.html'
    ), name='login'),
    path('logout/',logoutview,name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
