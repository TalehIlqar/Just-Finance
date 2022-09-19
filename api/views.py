from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from api.serializers import SubscriberSerializer
from django.utils.translation import ugettext_lazy as _
# Create your views here.


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