import boto3
import pandas as pd
import os


def get_meteor_files_from_s3(s3_bucket, meteor_data_file_download_location):

    for obj in s3_bucket.objects.all():
        meteor_data_filename = obj.key
        with open(os.path.join(meteor_data_file_download_location, meteor_data_filename), "wb") as meteor_data_file:
            s3_bucket.download_fileobj(meteor_data_filename, meteor_data_file)


if __name__ == "__main__":

    meteor_data_file_dir = "meteor_files"  # TODO: move this to config.json

    s3_bucket_name = "majorly-meteoric"  # TODO: move this to config.json
    s3 = boto3.resource('s3')
    s3_bucket = s3.Bucket(s3_bucket_name)

    if not os.path.exists(meteor_data_file_dir):
        os.makedirs(meteor_data_file_dir)

    get_meteor_files_from_s3(s3_bucket, meteor_data_file_dir)