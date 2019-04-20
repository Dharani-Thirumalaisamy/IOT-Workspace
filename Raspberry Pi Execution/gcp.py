# importing libraries

from google.cloud import storage
import os
import json
import time

# GCP credentials and making the connection
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "iot-project-235419-da501012ff0e.json"
storage_client = storage.Client()
buckets = list(storage_client.list_buckets())
bucket = storage_client.get_bucket("iot-project")

# function to upload the image ( filename and also what name to be given to the image when uploaded)
# this fucntion also makes the bucket public and gets the url of the bucket
def upload(project, bucket, image):
    FILENAME = image
    client = storage.Client(project)
    bucket = client.get_bucket(bucket)
    blob = bucket.blob('Test Image')
    blob.upload_from_filename(FILENAME, content_type='image/jpeg')
    blob.make_public()
    url = blob.public_url
    print("Image Uploaded")
    time.sleep(300)
