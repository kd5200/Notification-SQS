import boto3
import os
import json
from dotenv import load_dotenv
from django.core.mail import send_mail



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
    

def receive_message_from_sqs():
        
        load_dotenv()

        # Establishing a connection to Amazon sqs 
        sqs = boto3.client('sqs', region_name=os.getenv('REGION_NAME'))

        # Capturing the message from from my established sqs queue.
        response = sqs.receive_message(
            QueueUrl=os.getenv('SQS_QUEUE_URL'),
            MaxNumberOfMessages=1,
            VisibilityTimeout=10,
            WaitTimeSeconds=0
        )

        messages = response.get('Messages', [])


        # Receive every message within the queue one at a one (basically iterating through the que)
        for message in messages:
                # Extract message content
            message_body = message['test for HMI']

                # Send email
            send_email(message_body)

        # Delete message from SQS queue after processing
            sqs.delete_message(
                QueueUrl=os.getenv('SQS_QUEUE_URL'),
                ReceiptHandle=message['ReceiptHandle']
            )

def send_email(message_body):
    # Send email using Django's email functionality
    send_mail(
        'SQS Test',
        message_body,
        'kareemdavis18@yahoo.com',
        ['daviskareem92@gamil.com'],
        fail_silently=False,
    )




