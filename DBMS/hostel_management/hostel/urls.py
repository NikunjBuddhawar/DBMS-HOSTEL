from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking_view, name='booking'),
    path('success/', views.success_view, name='success'),  # This path now references the success_view
]
