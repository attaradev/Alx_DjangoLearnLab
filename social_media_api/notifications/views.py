from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification


class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.filter(read=False)
        # Mark notifications as read after retrieval
        notifications.update(read=True)
        data = [{"actor": n.actor.username, "verb": n.verb,
                 "target": str(n.target)} for n in notifications]
        return Response(data)
