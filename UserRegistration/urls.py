"""
URL configuration for UserRegistration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from accounts.views import home,login_view, logout_view, about, dashboard, contact, register, activation_invalid

urlpatterns = [
    path('login/', login_view, name='login'),  # Add this line
    path('logout/', logout_view, name='logout'),  # Add this line
    path('accounts/', include('django.contrib.auth.urls')),  # Include built-in auth URLs
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('activation_invalid/', activation_invalid, name='activation_invalid'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', home, name='home'),  # Ensure this line is present
]


