from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from core.api.serializers import SubscriberSerializer, ContactSerializer
from django.utils.translation import gettext_lazy as _

from core.models import Contact


class SubscriberAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {'success': True,
                       'message': _('Successfully subscribed.')}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {'status': 'success',
                       'message': _('Successfully sent.')}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
