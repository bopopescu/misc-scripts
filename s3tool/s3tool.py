import os

os.environ["AWS_ACCESS_KEY_ID"] = "***"
os.environ["AWS_SECRET_ACCESS_KEY"] = "***"

import boto
conn = boto.connect_s3()
mybucket = conn.get_bucket('***')
for item in mybucket.list():
    print item.name
