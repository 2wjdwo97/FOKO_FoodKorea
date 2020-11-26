import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/ubuntu/proj/CRAFT_image/My.json"
from google.cloud import vision
from google.cloud import translate_v2

def translate(string):
    client = translate_v2.Client()
    return client.translate(string, target_language='en')['translatedText']

def extractText(im):
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=im)
    return client.text_detection(image=image).text_annotations
