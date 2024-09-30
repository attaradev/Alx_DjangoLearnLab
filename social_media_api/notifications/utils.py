from .models import Notification
from django.contrib.contenttypes.models import ContentType


def create_notification(actor, verb, target):
    target_content_type = ContentType.objects.get_for_model(target)
    Notification.objects.create(
        actor=actor,
        verb=verb,
        target_content_type=target_content_type,
        target_object_id=target.pk,
        recipient=target.author
    )
