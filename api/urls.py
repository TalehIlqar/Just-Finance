from django.urls import path
from .views import SubscriberAPIView

urlpatterns = [
    path('subscriber/', SubscriberAPIView.as_view(), name='subscriberapi'),
]
