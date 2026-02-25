"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from allauth.account.views import SignupView

urlpatterns = [
    # 1. Staff Access
    path('admin/', admin.site.urls),
    # 2. The Landing Page (Direct Signup)
    path('', SignupView.as_view(), name='account_signup'),
    # 3. Medical App Logic
    path('clinical/', include('clinical.urls')),
    # 4. User Profile/Custom User Logic
    path('users/', include('users.urls')),
    # 5. AllAuth Authentication (Essential for AllAuth to work)
    path('accounts/', include('allauth.urls')),
    # 6. Redirect standard AllAuth signup to your root signup
    path('accounts/signup/', RedirectView.as_view(url="/")),
]
