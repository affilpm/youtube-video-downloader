from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerview, name='register'),
    path('verify/<str:email>/', views.verify_otp_view, name='verify_otp'),
    path('resend_otp/<str:email>/', views.resend_otp_view, name='resend_otp')
    
]
