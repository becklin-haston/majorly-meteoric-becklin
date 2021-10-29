import boto3
import pandas as pd
import os

meteor_data_file_dir = "meteor_files" # TODO: move this to config.json

if not os.path.exists(meteor_data_file_dir):
    os.makedirs(meteor_data_file_dir)

s3 = boto3.resource('s3')

s3_bucket_name = "majorly-meteoric" # TODO: move this to config.json

s3_bucket = s3.Bucket(s3_bucket_name)

for obj in s3_bucket.objects.all():
    meteor_data_filename = obj.key
    with open(os.path.join(meteor_data_file_dir, meteor_data_filename), "wb") as meteor_data_file:
        s3_bucket.download_fileobj(meteor_data_filename, meteor_data_file)