from django.shortcuts import render

from django.http import JsonResponse

import boto3
import requests
import json
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .sqs import send_notification_to_sqs
import os



def view(request):
    # Logic for your view
    # For example, you might want to send a notification when a certain event occurs

    # Construct your message
    notification_message = {
        'subject': 'Notification Subject',
        'body': 'testing que for HMI'
    }

    # Send the notification to SQS
    response = send_notification_to_sqs(notification_message)

    return JsonResponse({'status': 'Notification sent to SQS', 'response': response})




# The below "get notifications" function provides logic, 
# notifications variable being defined as all objects within our notification models.
# The data variable defines the order in which our data will be collected for each collection of a notification.  

# def get_notifications(request):
#     notifications = notification.objects.all()
#     data = [{'message': notification.message, 'recipient': notification.recipient, 'created_at': notification.created_at} for notification in notifications]
#     return JsonResponse(data, safe=False)


# The below function "send notification to sqs" provides logic for sending notifications to the SQS queue set up in AWS console.
# The sqs variable is a configuration of boto3 and identifying the AWS service we are sending our notification to.
# queue url variable contains the sqs que URL provided by AWS which is hidden in our environment variables file.
# 

# def send_notification_to_sqs(notification):
#     sqs = boto3.client('sqs')
#     queue_url = AWS_SQS_QUEUE_URL
#     sqs.send_message(QueueUrl=queue_url, MessageBody=notification.message)

# def create_notification(request):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         recipient = request.POST.get('recipient')
#         notifications = notification.objects.create(message=message, recipient=recipient)
#         send_notification_to_sqs(notifications)
#         return JsonResponse({'status': 'Notification created successfully'})
#     else:
#         return JsonResponse({'error': 'POST request required'})

# Create your views here.
