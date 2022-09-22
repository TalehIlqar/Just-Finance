from django.urls import path
from core.api.views import SubscriberAPIView

urlpatterns = [
    path('subscriber/', SubscriberAPIView.as_view(), name='subscriberapi'),
]
