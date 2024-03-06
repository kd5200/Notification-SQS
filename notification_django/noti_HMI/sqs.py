import boto3
import os
import json
from dotenv import load_dotenv
from django.core.mail import send_mail



def send_notification_to_sqs(message):

    try:
        load_dotenv()

        # 1. configure sqs configuration containing aws information using environment variables. 
        sqs = boto3.client('sqs',
                                aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
                                aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'),
                                region_name=os.getenv('REGION_NAME'),)
    

        # 2. configure variable for sqs queue URL
        queue_url = os.getenv('SQS_QUEUE_URL')



        # 3. Create a response variable that defines the logic of sending the message to the sqs queue.
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message)
        )

        return response
    
    except Exception as e:
        # Handle exception
        print("Error sending message to SQS:", e)
        return None
    



        






