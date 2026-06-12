from google.cloud import storage
from config.paths_config import *

client = storage.Client()

bucket = client.get_bucket('bucket_hrp2265')

print(bucket.name)

blob = bucket.blob('Hotel_Reservations.csv')

blob.download_to_filename(GOOG_FILE_PATH)