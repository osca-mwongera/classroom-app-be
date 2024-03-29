""" Core URL Configuration """
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_auth.views import PasswordResetConfirmView

API_V1 = 'api/v1/'
urlpatterns = [

    path('admin/', admin.site.urls),
    path(API_V1 + 'auth/', include('accounts.urls', namespace='accounts')),
    re_path(
        API_V1 + 'auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
    path(API_V1 + 'class/', include('classes.urls', namespace='classes'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
