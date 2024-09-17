from django.urls import path
from email_app.views import send_email,email_sent

urlpatterns = [
    path('',send_email,name='sendemail'),
    path('sent/',email_sent,name='emailsent'),
]
