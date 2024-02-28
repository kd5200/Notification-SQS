from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .sqs import send_notification_to_sqs


@receiver(post_migrate, sender=AppConfig)
def send_notification_on_startup(sender, **kwargs):
    # Construct the message for notification
    notification_message = {
        'subject': 'Django Project Initialized',
        'body': 'The Django project has been initialized.'
    }

    # Send the notification to SQS
    response = send_notification_to_sqs(notification_message)

    print("Notification sent to SQS:", response)