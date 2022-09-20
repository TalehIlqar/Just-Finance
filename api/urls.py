from django.urls import path
from . import views

path('subscriberapi/', views.SubscriberAPIView.as_view(), name='subscriberapi'),