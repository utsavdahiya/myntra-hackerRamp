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


def extract_objects(objects):
    boundaries = {}
    for object_ in objects:
        name = object_.name.lower()
        if (name == 'top' or name == 'shirt' or name == 'outerwear'):
            boundaries['top'] = object_.bounding_poly.normalized_vertices
        elif name == 'pants' or name == 'jeans':
            boundaries['bottom'] = object_.bounding_poly.normalized_vertices
        elif name == 'person':
            boundaries['person'] = object_.bounding_poly.normalized_vertices

    return boundaries

def get_object_boundaries(image_path):
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    vision_image = vision.Image(content=content)

    objects = client.object_localization(
        image=vision_image).localized_object_annotations

    object_boundaires = extract_objects(objects)
    object_boundaires['area_ratio'] = 0
    if ('person' in object_boundaires) and ('bottom' in object_boundaires):
        person = object_boundaires['person']
        bottom = object_boundaires['bottom']
        area_person = (person[1].x - person[0].x) * (person[2].y - person[1].y)
        area_bottom = (bottom[1].x - bottom[0].x) * (bottom[2].y - bottom[1].y)

        if area_person > 0 and area_bottom < area_person:
            object_boundaires['area_ratio'] = area_bottom / area_person

    return object_boundaires


def crop_and_save_image(image, boundary, image_name):
    width, height = image.size

    left = boundary[0].x * width
    top = boundary[0].y * height
    right = boundary[2].x * width
    bottom = boundary[2].y * height

    obj_img = image.crop((left, top, right, bottom))
    # obj_img.show()
    # print("Saving: "+ image_name)
    obj_img.save(image_name)

def get_training_set():
    with open('products', 'rb') as dump:
        prod_list = pickle.load(dump)

    prod_data_list = []
    image_to_boundary_map = {}
    # for i in range(len(prod_list)):
    for i in range(3):
        # if i % 20 == 0:
        #     with open('image_to_boundary.pkl', 'w+b') as boundary_db:
        #         image_to_boundary_file = boundary_db.read()
        product = prod_list[i]
        print("sno: " + str(i) + " pid: " + str(product['pid']))
        max_area = [0,""]
        #crop and save tops
        #find the full sie image
        #save data in data frame / csv
        cur_prod_list = []
        for j in range(len(product['images'])):
            product_df = {}
            product_df['pid'] = product['pid']

            image_url = product['images'][j]
            if image_url == '' or image_url is None:
                continue
            # print("url: " + image_url)
            image_suffix = str(product['pid']) + '~' + str(j) + '.jpg'
            original_image_path = download_image(image_url, image_suffix)
            object_boundaries = get_object_boundaries(original_image_path)
            cropped_image_path = 'resources/cropped/' + image_suffix
            if 'top' in object_boundaries:
                if max_area[0] < object_boundaries['area_ratio']:
                    max_area[0] = object_boundaries['area_ratio']
                    max_area[1] = original_image_path

                image = Image.open(original_image_path)
                crop_and_save_image(image, object_boundaries['top'], cropped_image_path)
                product_df['top'] = cropped_image_path
                image_to_boundary_map[original_image_path] = object_boundaries

            cur_prod_list.append(product_df)

        if max_area[0] > 0:
            full_image_path = max_area[1]
            # print("full image path: " + full_image_path)
            bottom_image_path = 'resources/bottom/' + str(product['pid']) + '.jpg'
            crop_and_save_image(Image.open(full_image_path), image_to_boundary_map[full_image_path]['bottom'],
                                bottom_image_path)
            for i in range(len(cur_prod_list)):
                product_df = cur_prod_list[i]
                product_df['bottom'] = bottom_image_path
                og_file_name = 'resources/original/' + str(product['pid']) + '~' + str(i) + '.jpg'
                if os.path.exists(og_file_name):
                    os.remove(og_file_name)


def download_image(image_url, img_name):
    image_path = 'resources/original/' + img_name
    response = requests.get(image_url, stream=True)
    with open(image_path, 'wb') as image_file:
        shutil.copyfileobj(response.raw, image_file)
    del response
    return image_path

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