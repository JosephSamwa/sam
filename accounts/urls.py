
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('activation_sent/', views.activation_sent, name='activation_sent'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    #path('support/', views.support, name='support'),
    path('login/', views.login_view, name='login'),  # Add this line
    path('logout/', views.logout_view, name='logout'),  # Add this line
    path('accounts/', include('django.contrib.auth.urls')),  # Include built-in auth URLs
]



