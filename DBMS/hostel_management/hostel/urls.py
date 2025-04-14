from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('booking/', views.booking_view, name='booking'),
    path('success/', views.success_view, name='success'),  # This path now references the success_view
    path('logout/', views.logout_view, name='logout'),
]
