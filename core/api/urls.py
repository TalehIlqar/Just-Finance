from django.urls import path
from core.api.views import SubscriberAPIView, ContactAPIView

urlpatterns = [
    path('subscriber/', SubscriberAPIView.as_view(), name='subscriberapi'),
    path('contact/', ContactAPIView.as_view(), name='contactapi'),
]
