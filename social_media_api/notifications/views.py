from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from rest_framework import status

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.filter(read=False)
        data = [
            {
                'id': notification.id,
                'actor': notification.actor.username,
                'verb': notification.verb,
                'timestamp': notification.timestamp,
                'target': str(notification.target) if notification.target else None,
            }
            for notification in notifications
        ]
        return Response(data, status=status.HTTP_200_OK)