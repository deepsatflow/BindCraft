import boto3 
import logging 
import os 
# read the list of existing bucket 
def list_bucket(): 
    try: 
        s3 = boto3.client('s3')
        response = s3.list_buckets() 
        if response: 
            print("Buckets exists...")
            for bucket in response["Buckets"]: 
                print(f'Bucket Name: {bucket["Name"]}')
    except Exception as e: 
        logging.error(e)
        return False 
    return True

list_bucket() 