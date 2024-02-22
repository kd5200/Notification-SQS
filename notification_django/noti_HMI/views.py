from django.shortcuts import render

from django.http import JsonResponse
import boto3
from notification_django.settings import *
from .models import notification


# def send_notification(request):
#     message_body = request.POST.get('message_body')
    
#     sqs_client = boto3.client('sqs',
#                               aws_access_key_id=AWS_ACCESS_KEY_ID,
#                               aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
#                               region_name=AWS_REGION_NAME)

#     queue_url = sqs_client.get_queue_url(QueueName=AWS_SQS_QUEUE_NAME)['QueueUrl']

#     response = sqs_client.send_message(
#         QueueUrl=queue_url,
#         MessageBody=message_body
#     )

#     return JsonResponse({'message_id': response['MessageId']})


# def create_notification(request):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         recipient = request.POST.get('recipient')
#         notifications = notification.objects.create(message=message, recipient=recipient)
#         # Code to send notification to SQS queue
#         return JsonResponse({'status': 'Notification created successfully'})
#     else:
#         return JsonResponse({'error': 'POST request required'})
    

def get_notifications(request):
    notifications = notification.objects.all()
    data = [{'message': notification.message, 'recipient': notification.recipient, 'created_at': notification.created_at} for notification in notifications]
    return JsonResponse(data, safe=False)


def send_notification_to_sqs(notification):
    sqs = boto3.client('sqs')
    queue_url = AWS_SQS_QUEUE_URL
    sqs.send_message(QueueUrl=queue_url, MessageBody=notification.message)

def create_notification(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        recipient = request.POST.get('recipient')
        notifications = notification.objects.create(message=message, recipient=recipient)
        send_notification_to_sqs(notifications)
        return JsonResponse({'status': 'Notification created successfully'})
    else:
        return JsonResponse({'error': 'POST request required'})

# Create your views here.
