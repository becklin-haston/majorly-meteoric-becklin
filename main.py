import boto3
import json
import pandas as pd
import os
import logging


def get_meteor_files_from_s3(bucket, meteor_data_file_download_location):

    for obj in bucket.objects.all():
        meteor_data_filename = obj.key
        with open(os.path.join(meteor_data_file_download_location, meteor_data_filename), "wb") as meteor_data_file:
            bucket.download_fileobj(meteor_data_filename, meteor_data_file)


if __name__ == "__main__":

    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

    with open("config.json", "r", encoding="utf-8") as config_json_file:
        config = json.load(config_json_file)

    meteor_data_file_dir_name = config["meteor_data_file_dir_name"]
    s3_bucket_name = config["s3_bucket_name"]
    s3 = boto3.resource('s3')
    s3_bucket = s3.Bucket(s3_bucket_name)

    if not os.path.exists(meteor_data_file_dir_name):
        os.makedirs(meteor_data_file_dir_name)

    get_meteor_files_from_s3(s3_bucket, meteor_data_file_dir_name)