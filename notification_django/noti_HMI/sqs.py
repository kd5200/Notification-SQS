import boto3
# from notification_sqs.settings import *
import requests
import os
import json
from dotenv import load_dotenv


def send_notification_to_sqs(message):

    try:
        load_dotenv()

        sqs = boto3.client('sqs',
                                aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
                                aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'),
                                region_name=os.getenv('REGION_NAME'),)
    

        queue_url = os.getenv('SQS_QUEUE_URL')




        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message)
        )

        return response
    
    except Exception as e:
        # Handle exception
        print("Error sending message to SQS:", e)
        return None
    

def receive_message_from_sqs(message):

    try:
        
        load_dotenv()

        sqs = boto3.client('sqs',
                                aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
                                aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'),
                                region_name=os.getenv('REGION_NAME'),)
    

        queue_url = os.getenv('SQS_QUEUE_URL')
