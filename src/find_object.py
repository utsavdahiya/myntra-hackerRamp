import io
import os
from PIL import Image
import shutil

import requests
import pickle
from collections import defaultdict

# Imports the Google Cloud client library
from google.cloud import vision

client = vision.ImageAnnotatorClient()

def extract_labels(img_url):

    vision_image, local_image = get_image(img_url)

    objects = client.object_localization(
        image=vision_image).localized_object_annotations

    labels = []
    # print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        labels.append(object_.name)
        # print('\n{} (confidence: {})'.format(object_.name, object_.score))
        # print('Normalized bounding polygon vertices: ')
        # for vertex in object_.bounding_poly.normalized_vertices:
        #     print(' - ({}, {})'.format(vertex.x, vertex.y))
    return labels

def get_image(url):
    image_path = 'resources/img_rand.jpg'
    response = requests.get(url, stream=True)
    with open(image_path, 'wb') as image_file:
        shutil.copyfileobj(response.raw, image_file)
    del response
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    vision_image = vision.Image(content=content)
    local_image = Image.open(image_path)
    return vision_image, local_image

def get_default_value():
    return 0

def get_similar_style(image_path):
    pass

def find_labels():
    with open('products', 'rb') as dump:
        prod_list = pickle.load(dump)
        labels = defaultdict(get_default_value)
        for i in range(len(prod_list)):
            img_url = prod_list[i]['images'][0]
            print(img_url)
            cur_labels = extract_labels(img_url)
            for label in cur_labels:
                labels[label] += 1

        print(labels)