from django.shortcuts import render

from django.http import JsonResponse
import boto3
from notification_django.settings import *

def send_notification(request):
    message_body = request.POST.get('message_body')
    
    sqs_client = boto3.client('sqs',
                              aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                              region_name=AWS_REGION_NAME)

    queue_url = sqs_client.get_queue_url(QueueName=AWS_SQS_QUEUE_NAME)['QueueUrl']

    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )

    return JsonResponse({'message_id': response['MessageId']})

# Create your views here.
