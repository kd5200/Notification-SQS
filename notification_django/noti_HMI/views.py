from django.shortcuts import render
from django.http import JsonResponse
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .sqs import send_notification_to_sqs, receive_message_from_sqs, send_email




def view(request):
    # Logic for view
    # For example, you might want to send a notification when a certain event occurs

    # Construct  message
    notification_message = {
        'subject': 'Notification Subject',
        'body': 'testing que for HMI    '
    }

    # Send the notification to SQS
    response = send_notification_to_sqs(notification_message)


    return JsonResponse({'status': 'Notification sent to SQS', 'response': response})



# Will I need to create another function within view file to receive and send message to email?

# Create your views here.
