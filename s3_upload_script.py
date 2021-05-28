import logging
import boto3
from botocore.exceptions import ClientError
import os, sys 


#CRED for S3
ACCESS_KEY=''
SECRET_KEY=''


def s3_upload(PATH,EXT, s3_bucket, ACCESS_KEY, SECRET_KEY):

    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)



    try:
        if os.path.exists(PATH):
            DIR = os.chdir(PATH)

            print("Uploading in-progress...")
            for file in os.listdir(DIR):
                if EXT in file:
                    upload_file_bucket = s3_bucket
                    upload_file_key = 'python/' + str(file)
                    s3_client.upload_file(file, upload_file_bucket, upload_file_key)
                    
            
            print('Upload Completed..')
            
        else:
            print("PATH Not Exist")
            sys.exit()

    except ClientError as e:
        error = logging.error(e)
        print(error)

if __name__ == '__main__':

    req_path = input("Enter a PATH: ")
    req_file = input("Enter file extension to be uploaded: ")

    s3_upload(req_path, req_file, "raymart-dummy-dump", ACCESS_KEY, SECRET_KEY)





