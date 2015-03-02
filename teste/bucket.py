from django.conf import settings

from boto.s3.connection import S3Connection

from boto.s3.key import Key

conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)

conn.lookup(settings.AWS_STORAGE_BUCKET_NAME)

bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)

k = Key(bucket)
k.key = "rocklee-sd"
k.get_contents_as_string()
