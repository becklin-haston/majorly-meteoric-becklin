import boto3
import pandas as pd

s3 = boto3.resource('s3')

s3_bucket_name = "majorly-meteoric" # TODO: move this to config.json

s3_bucket = s3.Bucket(s3_bucket_name)

for obj in s3_bucket.objects.all():
    print(obj)