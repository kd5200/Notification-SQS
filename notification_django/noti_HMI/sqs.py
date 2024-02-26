import boto3
from notification_django.settings import *
import requests
import json

def send_notification_to_sqs(message):
    # message_body = request.POST.get('message_body')
    
    sqs = boto3.client('sqs',
                              aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                              region_name=AWS_REGION_NAME)

    queue_url = AWS_SQS_QUEUE_URL

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message)
    )

    return response