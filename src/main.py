# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import io
import os
from PIL import Image
import pickle

import find_object
import similar_style

# Imports the Google Cloud client library
from google.cloud import vision

image_path = 'resources/img_1.png'
product_list = []

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def label_detection():
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath(image_path)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)


    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)

    objects = client.object_localization(
        image=image).localized_object_annotations

    im = Image.open(image_path)
    width, height = im.size
    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        left = object_.bounding_poly.normalized_vertices[0].x * width
        top = object_.bounding_poly.normalized_vertices[0].y * height
        right = object_.bounding_poly.normalized_vertices[2].x * width
        bottom = object_.bounding_poly.normalized_vertices[2].y * height
        obj_img = im.crop((left, top, right, bottom))
        obj_img.show()
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))

def save_data(data):
    dbfile = open('products', 'ab')

    print("saving " + str(len(data)) + " products")
    pickle.dump(data, dbfile)
    dbfile.close()

def parse_response(resp):
    for product in resp['products']:
        prod = {
            'url': product['landingPageUrl'],
            'pid': product['productId'],
        }
        prod['images'] = [img['src'] for img in product['images'] if len(img)>0]
        product_list.append(prod)

    print("prod list size: " + str(len(product_list)))


def test_request():
    import requests

    cookies = {
        '_pv': 'default',
        'dp': 'd',
        'at': 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pTm1KaFlqVm1aV0V0TWpKa01DMHhNV1ZrTFRneVlURXRaV1V3T0RZNU9EVXpOekF6SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUyTnpZNE1ETTBNRGNzSW1semN5STZJa2xFUlVFaWZRLlMtTnlVUkFQeGFlU3VyWTdYb01YRzVKNUJHUUNaRFA2cm9VOWRwUjFLVk0=',
        'bc': 'true',
        'lt_timeout': '1',
        'lt_session': '1',
        'AKA_A2': 'A',
        'bm_sz': '89DC934590A7EABAA83DC786CD9F7561~YAAQstxVuJGgLcmCAQAAO85MyhDBTml7nNHIePnWTIpRMVpKCXnFp6HthLLJb5R7WvBYaPfv8cUFXdma2dzMWQI7BTM+JgD+8Cj+YtBn9ffb/MPn2dFHIvKwZf0mIkqKcbiMLuxnaeLoq/HDTaT56aS1sROF8ndsAx8OJldbSAoMoRicFFFjFB/ctQmguTsPzTrGiMrrcuRhzd3h0A2glen4myMm91pN4XG2NRFMGrONE1xLyt0KdoJzkaRgMOe0gGgdQGw26z5lvvq2C/LYfy8OwjElVek4XxqAovkOknyQl+o=~4536630~4273473',
        'bm_mi': '7D6D9ED9A6700D0890C56AB8810E667D~YAAQstxVuLGgLcmCAQAASs9MyhAwd3Ig7Iw3fCg/72ve7y0MbFsAYGM0LlrSLaD9zsUiuSXQHHLUaUpDNrOzSyvOcCPYQBFMEV+lrWE5QnQCasJ8SPMJJKsjEMPO4rlx0yKYPymT8zF8k0u6OhNbtWvit7zle2TkU8VyBfhfvfbj9K+Y3P1cJ6mNGlx+JkUCBJAnkdPPYyRLhn7yMFYwAHAJjGXXE0CE/mNIOlfsxHdW2k1ScZscAfjYshRvAdbKdlQhUZKSEdjXy+O2Nu3RFpIwis0HHVZ3Z9JXofwS0DZqn64aeFcrLPLGJkLg0MJmeQ2QVHX/UP1BD6B6yQ5IEHWyhz15dEG1smRzHM5xPzLAMVh7vMmtEg==~1',
        '_d_id': '045f724e-07d9-4314-a788-fb5cb256e2bb',
        '_ma_session': '%7B%22id%22%3A%2254427949-090d-459b-b242-58529bc2deb9-045f724e-07d9-4314-a788-fb5cb256e2bb%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D',
        'mynt-eupv': '1',
        'mynt-ulc-api': 'pincode%3A110054',
        'mynt-loc-src': 'expiry%3A1661252847630%7Csource%3AIP',
        'microsessid': '167',
        '_xsrf': '7vt6eUZEEDJ5k1ynOdyPlzrbq9JebSOI',
        'AMP_TOKEN': '%24NOT_FOUND',
        '_ga': 'GA1.2.1188662099.1661251408',
        '_gid': 'GA1.2.1249469276.1661251408',
        '_gat': '1',
        '_gcl_au': '1.1.262351802.1661251408',
        '_dc_gtm_UA-1752831-18': '1',
        'tvc_VID': '1',
        '_fbp': 'fb.1.1661251408567.267116210',
        '_mxab_': 'checkout.selective%3Denabled%3Bconfig.bucket%3Dregular%3Bcheckout.couponUpsell%3Denabled%3Bcheckout.attachedProducts%3Denabled%3Bcheckout.donation%3Denabled%3Bpdp.expiry.date%3Denabled',
        'utm_track_v1': '%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1661251421%2C%22trackend%22%3A1661251481%7D',
        'utrid': 'SQxCVVkHdgFScmB%2FHgBAMCMyNzY0MjAwMTk3JDI%3D.d7d7b91b319c867ace5e4b7fc10c810d',
        'user_session': 'z4iLz2e6aQ0gTEg7yvuZ0Q.dJcqbysP5cyApcBOZXGkYQaJ5BgJfQSe9mLmtvLMa273fxewF9Gq5g66YSSsCtptzD5eIhg7gsMDCtvDOmx3kQdb52HkoFkhGEH_6Xo_FNzauPsUt5PRbz1K1_nv8EEM5vtYVaWJtgVnDGsJKOhq1A.1661251407817.86400000.RbxX4Nu8DJ5QQnHIiYM1LB3er5lJVVvvGzr_otJk0b0',
        'bm_sv': '68767805186545DF067073FA032F0D70~YAAQstxVuNGlLcmCAQAAvQVNyhCTcrp5kid6xC9PoUEs6QdYVgcEnqkU3I4fiJRKZ3Vmev3jtGqVehY2PKTlYxHxnSSMIwvw+blVRspKWA+d3Nh8KnquSlF/KAo2HD7Sg8PmR1Yvx+XDkLKuIIDOkVaUTmFRzT7JeuwTNjR/BGzYf0LOKPUIruM1pTx58oXRMhbZnirskJ4A0XNhJmIggroyOP89I2UfqmQXddIoUyg1F5D0CQA+DzDykePQ+zyK~1',
        '_abck': 'F54E5A799E5205C25A19C46E48F5F1F8~0~YAAQstxVuOqlLcmCAQAA1QZNygh7f6/J+7jt0GncEnpYmXDnJgKEglJwR4sXVzZqkntQZkjpAvSvnYp2Ea6uAyKMtYAorMgiOMKsCPE2W6Dfp3KQJb80+zzhZmf9Wgybp47n+SzE6a/yVIWMv4EsTbN/RNuFT1ZadFsATpjXq4iMhTzTxiUgYZk7WwJK+moFjcuLf6BpXQ5wFHXpfW2yGA8Fle+yghSwZrBM5xKQ+pP/fH9nCrpJplUjoM8GD0V0Q/LWywjH0jxLgd7tCNwkpAore8E58Dd+Vri3JibpKuu6wPCLJHJo9IgU6/9oxUnMGTwbj01U+KcJSZqaCqF6wvP6ONHYiBHTMJ+8wRzEUhR8g9KHiwb5my5qNs37deH7bg9kSsPZVMRGtJiULv+R/wfFQKF0wgOh~-1~||1-VpbIDWwuNM-1-10-1000-2||~1661254929',
        'cto_bundle': 'oNAam19hU0o0VkhvNSUyRlU0JTJGS2tMNlFVdlZWMlFZU3lWb21QRTFKQnMzJTJGd2loJTJGWjNaQjFQVFdBT0lVOHpVZEN5OTNzR3BrNlQ3ZHlUNlRlZkRSeFVCNkRBNlZ0OE9oYnhCdDFGc2FadjREcVYwUkUwNmJ2TlFuYlpIOXpTUXBTSDBRSFVO',
        'ak_RT': '"z=1&dm=myntra.com&si=32b49b79-65af-4a3c-875e-e53baf4afeb9&ss=l7627bme&sl=1&tt=1wp&rl=1&ld=1wq"',
        '_cc_id': '87e9ecc08311b9b1e283cc4174320a9e',
        'panoramaId_expiry': '1661337822945',
        'ak_bmsc': '3100116A61A25DDBD988C3CE7DC9A6E0~000000000000000000000000000000~YAAQstxVuNCmLcmCAQAAmxFNyhBOfM3Gr4DsMRlHqhhUIPy4ajEnIR6cksUy46qeHjIIou+BGiGaamp2WtZIaxqKYChKhzqx/CynKSvZAi3m6DrSwHSdtgOXeGxCO9nAZMrxyBLe8BGajc9O76HPMFBoj6h+Zo3cXW1e3Ihnhq56ckAHWbbPET2cq85BHcweIVB43K0nXh0r3JDWhd3RoxRcLIT+qGEXivxbvjyO95wOoB9AG9PMJih9zlVKTkuZ5l1RWRkr2g54hMEB/MtWF10sE6XfYYNn7Crw/FBCrGX11ItZQ94pEonMOei5Wy9eB8hqmrAEjQrHe5Oz3rF/TMf7egNu00uBbS5R0xbZiwTKDqPDd8dbhy+YVU0sbBakmQjFxlZPMQ+t6UEp46BkUONFJfezFQrQmnnbPU7oUTrvDSNBlOZVnsFVD+f0o3n9VOeBXqy1DUvzd7O6FFf+xVtUKq2ypw==',
    }

    headers = {
        'authority': 'www.myntra.com',
        'accept': 'application/json',
        'accept-language': 'en-GB,en;q=0.9',
        'app': 'web',
        'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_pv=default; dp=d; at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pTm1KaFlqVm1aV0V0TWpKa01DMHhNV1ZrTFRneVlURXRaV1V3T0RZNU9EVXpOekF6SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUyTnpZNE1ETTBNRGNzSW1semN5STZJa2xFUlVFaWZRLlMtTnlVUkFQeGFlU3VyWTdYb01YRzVKNUJHUUNaRFA2cm9VOWRwUjFLVk0=; bc=true; lt_timeout=1; lt_session=1; AKA_A2=A; bm_sz=89DC934590A7EABAA83DC786CD9F7561~YAAQstxVuJGgLcmCAQAAO85MyhDBTml7nNHIePnWTIpRMVpKCXnFp6HthLLJb5R7WvBYaPfv8cUFXdma2dzMWQI7BTM+JgD+8Cj+YtBn9ffb/MPn2dFHIvKwZf0mIkqKcbiMLuxnaeLoq/HDTaT56aS1sROF8ndsAx8OJldbSAoMoRicFFFjFB/ctQmguTsPzTrGiMrrcuRhzd3h0A2glen4myMm91pN4XG2NRFMGrONE1xLyt0KdoJzkaRgMOe0gGgdQGw26z5lvvq2C/LYfy8OwjElVek4XxqAovkOknyQl+o=~4536630~4273473; bm_mi=7D6D9ED9A6700D0890C56AB8810E667D~YAAQstxVuLGgLcmCAQAASs9MyhAwd3Ig7Iw3fCg/72ve7y0MbFsAYGM0LlrSLaD9zsUiuSXQHHLUaUpDNrOzSyvOcCPYQBFMEV+lrWE5QnQCasJ8SPMJJKsjEMPO4rlx0yKYPymT8zF8k0u6OhNbtWvit7zle2TkU8VyBfhfvfbj9K+Y3P1cJ6mNGlx+JkUCBJAnkdPPYyRLhn7yMFYwAHAJjGXXE0CE/mNIOlfsxHdW2k1ScZscAfjYshRvAdbKdlQhUZKSEdjXy+O2Nu3RFpIwis0HHVZ3Z9JXofwS0DZqn64aeFcrLPLGJkLg0MJmeQ2QVHX/UP1BD6B6yQ5IEHWyhz15dEG1smRzHM5xPzLAMVh7vMmtEg==~1; _d_id=045f724e-07d9-4314-a788-fb5cb256e2bb; _ma_session=%7B%22id%22%3A%2254427949-090d-459b-b242-58529bc2deb9-045f724e-07d9-4314-a788-fb5cb256e2bb%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; mynt-eupv=1; mynt-ulc-api=pincode%3A110054; mynt-loc-src=expiry%3A1661252847630%7Csource%3AIP; microsessid=167; _xsrf=7vt6eUZEEDJ5k1ynOdyPlzrbq9JebSOI; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1188662099.1661251408; _gid=GA1.2.1249469276.1661251408; _gat=1; _gcl_au=1.1.262351802.1661251408; _dc_gtm_UA-1752831-18=1; tvc_VID=1; _fbp=fb.1.1661251408567.267116210; _mxab_=checkout.selective%3Denabled%3Bconfig.bucket%3Dregular%3Bcheckout.couponUpsell%3Denabled%3Bcheckout.attachedProducts%3Denabled%3Bcheckout.donation%3Denabled%3Bpdp.expiry.date%3Denabled; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1661251421%2C%22trackend%22%3A1661251481%7D; utrid=SQxCVVkHdgFScmB%2FHgBAMCMyNzY0MjAwMTk3JDI%3D.d7d7b91b319c867ace5e4b7fc10c810d; user_session=z4iLz2e6aQ0gTEg7yvuZ0Q.dJcqbysP5cyApcBOZXGkYQaJ5BgJfQSe9mLmtvLMa273fxewF9Gq5g66YSSsCtptzD5eIhg7gsMDCtvDOmx3kQdb52HkoFkhGEH_6Xo_FNzauPsUt5PRbz1K1_nv8EEM5vtYVaWJtgVnDGsJKOhq1A.1661251407817.86400000.RbxX4Nu8DJ5QQnHIiYM1LB3er5lJVVvvGzr_otJk0b0; bm_sv=68767805186545DF067073FA032F0D70~YAAQstxVuNGlLcmCAQAAvQVNyhCTcrp5kid6xC9PoUEs6QdYVgcEnqkU3I4fiJRKZ3Vmev3jtGqVehY2PKTlYxHxnSSMIwvw+blVRspKWA+d3Nh8KnquSlF/KAo2HD7Sg8PmR1Yvx+XDkLKuIIDOkVaUTmFRzT7JeuwTNjR/BGzYf0LOKPUIruM1pTx58oXRMhbZnirskJ4A0XNhJmIggroyOP89I2UfqmQXddIoUyg1F5D0CQA+DzDykePQ+zyK~1; _abck=F54E5A799E5205C25A19C46E48F5F1F8~0~YAAQstxVuOqlLcmCAQAA1QZNygh7f6/J+7jt0GncEnpYmXDnJgKEglJwR4sXVzZqkntQZkjpAvSvnYp2Ea6uAyKMtYAorMgiOMKsCPE2W6Dfp3KQJb80+zzhZmf9Wgybp47n+SzE6a/yVIWMv4EsTbN/RNuFT1ZadFsATpjXq4iMhTzTxiUgYZk7WwJK+moFjcuLf6BpXQ5wFHXpfW2yGA8Fle+yghSwZrBM5xKQ+pP/fH9nCrpJplUjoM8GD0V0Q/LWywjH0jxLgd7tCNwkpAore8E58Dd+Vri3JibpKuu6wPCLJHJo9IgU6/9oxUnMGTwbj01U+KcJSZqaCqF6wvP6ONHYiBHTMJ+8wRzEUhR8g9KHiwb5my5qNs37deH7bg9kSsPZVMRGtJiULv+R/wfFQKF0wgOh~-1~||1-VpbIDWwuNM-1-10-1000-2||~1661254929; cto_bundle=oNAam19hU0o0VkhvNSUyRlU0JTJGS2tMNlFVdlZWMlFZU3lWb21QRTFKQnMzJTJGd2loJTJGWjNaQjFQVFdBT0lVOHpVZEN5OTNzR3BrNlQ3ZHlUNlRlZkRSeFVCNkRBNlZ0OE9oYnhCdDFGc2FadjREcVYwUkUwNmJ2TlFuYlpIOXpTUXBTSDBRSFVO; ak_RT="z=1&dm=myntra.com&si=32b49b79-65af-4a3c-875e-e53baf4afeb9&ss=l7627bme&sl=1&tt=1wp&rl=1&ld=1wq"; _cc_id=87e9ecc08311b9b1e283cc4174320a9e; panoramaId_expiry=1661337822945; ak_bmsc=3100116A61A25DDBD988C3CE7DC9A6E0~000000000000000000000000000000~YAAQstxVuNCmLcmCAQAAmxFNyhBOfM3Gr4DsMRlHqhhUIPy4ajEnIR6cksUy46qeHjIIou+BGiGaamp2WtZIaxqKYChKhzqx/CynKSvZAi3m6DrSwHSdtgOXeGxCO9nAZMrxyBLe8BGajc9O76HPMFBoj6h+Zo3cXW1e3Ihnhq56ckAHWbbPET2cq85BHcweIVB43K0nXh0r3JDWhd3RoxRcLIT+qGEXivxbvjyO95wOoB9AG9PMJih9zlVKTkuZ5l1RWRkr2g54hMEB/MtWF10sE6XfYYNn7Crw/FBCrGX11ItZQ94pEonMOei5Wy9eB8hqmrAEjQrHe5Oz3rF/TMf7egNu00uBbS5R0xbZiwTKDqPDd8dbhy+YVU0sbBakmQjFxlZPMQ+t6UEp46BkUONFJfezFQrQmnnbPU7oUTrvDSNBlOZVnsFVD+f0o3n9VOeBXqy1DUvzd7O6FFf+xVtUKq2ypw==',
        'referer': 'https://www.myntra.com/men-formal-shirts?p=2',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-location-context': 'pincode=110054;source=IP',
        'x-meta-app': 'channel=web',
        'x-myntra-app': 'deviceID=045f724e-07d9-4314-a788-fb5cb256e2bb;customerID=;reqChannel=web;',
        'x-myntraweb': 'Yes',
        'x-requested-with': 'browser',
    }

    params = {
        'p': '0',
        'rows': '100',
        'o': '0',
        'plaEnabled': 'false',
    }

    offset = 0
    rows = 100
    p = 0
    for i in range(10):
        print("send")
        response = requests.get('https://www.myntra.com/gateway/v2/search/men-formal-shirts', params=params, cookies=cookies, headers=headers)
        print("statusCode: " + str(response.status_code))
        print("Num products: "+ str(len(response.json()['products'])))
        parse_response(response.json())

        offset += rows
        params['o'] = str(offset)
        params['p'] = str(i)

    print("complete")
    save_data(product_list)

def read_data():
    dbfile = open('products', 'rb')
    prod_list = pickle.load(dbfile)
    print("num prod: " + str(len(prod_list)))
    for i in range(0,50,4):
        img_url = prod_list[i]['images'][0]
        print(img_url)
        find_object.extract_labels(img_url)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # label_detection()
    # test_request()
    # read_data()
    # img_url = "http://assets.myntassets.com/assets/images/14093094/2021/5/18/58ca00e0-72f8-478d-b6c1-f2fa3f3c78da1621339386853BlackberrysMenBlackB95TaperedFitSolidRegularTrousersTshirtsH1.jpg"
    # extract_labels(img_url)
    # vis_image, loc_image = find_object.get_image(img_url)
    # print("size: " + str(loc_image.size))
    # find_object.find_labels()
    find_object.get_training_set()

    # similar_style.get_similar_style("img_1.png")
    # similar_style.get_similar_2("")
    # similar_style.postman()
    # similar_style.postman_http()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
