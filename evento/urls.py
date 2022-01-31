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


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from . import views


from account.views import UserRegisterAV, RegisterOtpAV, ConfirmRegisterOtpAV, UsersListAV, ForgotPhoneCheckAV, ConfirmForgetOtpAV, ForgetChangePasswordAV
from vendor.views import VendorRegisterCheckAV, VendorRegisterAV, VendorUpdateAV, VendorHomePageAV


urlpatterns = [
    path('admin/', admin.site.urls),

    path('docs/',include_docs_urls(title='EventoAPI')),
    path('schema', get_schema_view(
        title="EventoAPI",
        description="API for evento app",
        version="1.0.0"
    ), name='openapi-schema'),

    # path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('api/register/', UserRegisterAV.as_view(), name='register'),
    path('api/register/otp/', RegisterOtpAV.as_view(), name='register-otp-verify'),
    path('api/register/confirm/', ConfirmRegisterOtpAV.as_view(), name='register-otp-confirm'),
    path('api/forget/phonecheck/', ForgotPhoneCheckAV.as_view(), name='forget-phone-check'),
    path('api/forget/otpconfirm/', ConfirmForgetOtpAV.as_view(), name='forget-otp-confirm'),
    path('api/forget/changepass/', ForgetChangePasswordAV.as_view(), name='forget-password-change'),
    path('api/users/list/', UsersListAV.as_view(), name='users-list'),

    path('api/vendor/check/', VendorRegisterCheckAV.as_view(), name='check-user-as-vendor'),
    path('api/vendor/register/', VendorRegisterAV.as_view(), name='vendor-register'),
    path('api/vendor/home/', VendorHomePageAV.as_view(), name='vendor-homepage'),

    path('api/vendor/update/', VendorUpdateAV.as_view(), name='vendor-update'),
    # path('api/vendor/subscription/', VendorSubscriptionAV.as_view(), name='vendor-subscription'),




    path('testing/', views.testing, name='testing' ),

]

urlpatterns += static(settings.MEDIA_URL, documnent_root=settings.MEDIA_ROOT)