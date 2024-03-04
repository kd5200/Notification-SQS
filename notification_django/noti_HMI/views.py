from django.shortcuts import render
from django.http import JsonResponse
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .sqs import send_notification_to_sqs, receive_message_from_sqs, send_email




def view(request):
    # Construct  message
    notification_message = {
        'subject': 'Notification Subject',
        'body': 'testing queue for HMI    '
    }

    # Send the notification to SQS
    response = send_notification_to_sqs(notification_message)


    return JsonResponse({'status': 'Notification sent to SQS', 'response': response})


# Function to receive message from queue.
def view_redirect(request):
    # Receive message from SQS
    # Within this receive message from sqs queue function it should handke sending the messag from there.
    receive_message_from_sqs()

    return JsonResponse({'status': 'From queue to email success'})
 
# Create a function to utilize Amazon SNS once a message is received from the queue.

# def email_noti(request):





# Create your views here.
