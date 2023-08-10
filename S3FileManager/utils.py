import os

import boto3

from dotenv import load_dotenv, find_dotenv

_= load_dotenv(find_dotenv())

 

 

# configure credentials for AWS s3 access

client = boto3.client('s3',

                      aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),

                      aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),

                      aws_session_token=os.getenv('AWS_SESSION_TOKEN'))