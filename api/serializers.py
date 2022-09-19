from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import Subscriber



class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('email',)