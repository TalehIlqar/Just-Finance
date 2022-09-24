from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import Subscriber, Contact


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('email',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'phone_number', 'category', 'message')
