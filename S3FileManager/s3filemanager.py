import os
import boto3
import utils
from botocore.exceptions import ClientError

class S3FileManager:
    
    def upload_file_to_s3(local_file_path, target_bucket_name, target_object_name=None):
        # Use local_file_path as object name if target_object_name is not specified
        if target_object_name is None:
            target_object_name = os.path.basename(local_file_path)
        
        s3_client = boto3.client('s3')
        try:
            s3_client.upload_file(local_file_path, target_bucket_name, target_object_name)
        except ClientError as e:
            utils.error(e)
            return False
        return True
    
    def download_file_from_s3(target_bucket_name, source_object_name, local_file_path):
        s3_client = boto3.client('s3')
        try:
            s3_client.download_file(target_bucket_name, source_object_name, local_file_path)
        except ClientError as e:
            utils.error(e)

class S3AccessControl:
    
    def get_bucket_access_control_list(target_bucket_name):
        s3_client = boto3.client('s3')
        result = s3_client.get_bucket_acl(Bucket=target_bucket_name)
        return result

def main():
    file_manager = S3FileManager()
    access_control = S3AccessControl()
    
    # Upload a file to S3
    file_manager.upload_file_to_s3('local_file_path', 'target_bucket_name')
    
    # Download a file from S3
    file_manager.download_file_from_s3('target_bucket_name', 'source_object_name', 'local_file_path')
    
    # Get S3 bucket access control list
    access_control_list = access_control.get_bucket_access_control_list('target_bucket_name')
    print(access_control_list)

if __name__ == "__main__":
    main()
