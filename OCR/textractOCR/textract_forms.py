import os
import re
import sys
import json
import boto3

from io import BytesIO
from pdf2image import convert_from_path, convert_from_bytes

image_extensions = ['png', 'jpg', 'jpeg']

def get_kv_map(bytes_string, access_key_id, secret_access_key, region_name):
    """Retreive Key, Value and Blocks from byte-string"""
    client = boto3.client('textract',
                      aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key,
                      region_name=region_name)
    response = client.analyze_document(Document={'Bytes': bytes_string}, FeatureTypes=['FORMS'])

    blocks=response['Blocks']
       
    key_map = {}
    value_map = {}
    block_map = {}

    for block in blocks:
        block_id = block['Id']
        block_map[block_id] = block
        if block['BlockType'] == "KEY_VALUE_SET":
            if 'KEY' in block['EntityTypes']:
                key_map[block_id] = block
            else:
                value_map[block_id] = block

    return key_map, value_map, block_map

def get_kv_relationship(key_map, value_map, block_map):
    """Return key-value pair"""
    kvs = {}
    for block_id, key_block in key_map.items():
        value_block = find_value_block(key_block, value_map)
        key = get_text(key_block, block_map)
        val = get_text(value_block, block_map)
        kvs[key] = val

    return kvs


def find_value_block(key_block, value_map):
    """Return block of values for corresponding block of keys"""
    for relationship in key_block['Relationships']:
        if relationship['Type'] == 'VALUE':
            for value_id in relationship['Ids']:
                value_block = value_map[value_id]

    return value_block


def get_text(result, blocks_map):
    """Return text for key/value present in blocks_map"""
    text = ''
    if 'Relationships' in result:
        for relationship in result['Relationships']:
            if relationship['Type'] == 'CHILD':
                for child_id in relationship['Ids']:
                    word = blocks_map[child_id]
                    if word['BlockType'] == 'WORD':
                        text += word['Text'] + ' '
    return text

def search_value(kvs, search_key):
    """Helper function to return values corresponding 'search_key' """
    for key, value in kvs.items():
        if re.search(search_key, key, re.IGNORECASE):
            return value
        else:
            return f'Nothing match for {search_key}'

def get_forms_from_image(image, access_key_id, secret_access_key, region_name):
    """Return forms for a given image file"""
    with open(image, 'rb') as file_:
        img_test = file_.read()
        bytes_string = bytearray(img_test)

    key_map, value_map, block_map = get_kv_map(bytes_string)
    kvs = get_kv_relationship(key_map, value_map, block_map)
    return kvs

def get_forms_from_pdf(file_name, access_key_id, secret_access_key, region_name):
    """Return forms for a given pdf document"""
    images = convert_from_path(file_name)

    all_forms = list()
    for i, image in enumerate(images):
        fname = 'page ' + str(i+1) + '.png'
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
    
        key_map, value_map, block_map = get_kv_map(img_byte_arr, access_key_id, secret_access_key, region_name)
        form = get_kv_relationship(key_map, value_map, block_map)
        all_forms.append(form)
    return all_forms

if __name__ == "__main__":

    file_name = sys.argv[1]
    name, extn = file_name.split('.')

    if extn in image_extensions:
        forms = get_forms_from_image(file_name, access_key_id, secret_access_key, region_name)

    elif extn == "pdf":
        forms = get_forms_from_pdf(file_name, access_key_id, secret_access_key, region_name)

    json.dump(forms, open(f'{name}_form.json', 'w'))
