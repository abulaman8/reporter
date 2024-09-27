from django.contrib import admin
from django.urls import path, include
from base.views import CustomSignupView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('', include('base.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
