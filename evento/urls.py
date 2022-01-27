"""evento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


from account.views import UserRegisterAV, RegisterOtpAV, ConfirmRegisterOtpAV
from vendor.views import VendorRegisterAV, VendorUpdateAV, VendorSubscriptionAV


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/',include_docs_urls(title='EventoAPI')),
    path('schema', get_schema_view(
        title="EventoAPI",
        description="API for evento app",
        version="1.0.0"
    ), name='openapi-schema'),

    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


    path('api/register/', UserRegisterAV.as_view(), name='register'),
    path('api/register/otp/', RegisterOtpAV.as_view(), name='register-otp-verify'),
    path('api/register/confirm/', ConfirmRegisterOtpAV.as_view(), name='register-otp-confirm'),

    path('api/vendor/register/', VendorRegisterAV.as_view(), name='vendor-register'),
    path('api/vendor/update/', VendorUpdateAV.as_view(), name='vendor-update'),
    path('api/vendor/subscription/', VendorSubscriptionAV.as_view(), name='vendor-subscription'),

]
