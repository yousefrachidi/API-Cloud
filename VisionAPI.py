import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "apikey.json"

client = vision.ImageAnnotatorClient()

print('ok')