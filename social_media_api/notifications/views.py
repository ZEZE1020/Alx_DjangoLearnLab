from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer
from django.shortcuts import render

# Create your views here.


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(recipient=user).order_by('-timestamp')