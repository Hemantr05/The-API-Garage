import re
import cv2
import json
import pytesseract
import matplotlib.pyplot as plt 

async def json_response(img):
    """Returns jsonified response for given invoice"""
    img = cv2.imreade(img)
    extracted_text = pytesseract.image_to_string(img, lang = 'deu')

    receipt_ocr = {}
    splits = extracted_text.splitlines()
    restaurant_name = splits[0] + '' + splits[1]

    # regex for date. The pattern in the receipt is in 30.07.2007 in DD:MM:YYYY
    date_pattern = r'(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d'
    date = re.search(date_pattern, extracted_text).group()
    receipt_ocr['date'] = date

    # get lines with chf
    lines_with_chf = []
    for line in splits:
        if re.search(r'CHF',line):
            lines_with_chf.append(line)


    items = []
    for line in lines_with_chf:
        if re.search(r'Incl',line):
            continue
        if re.search(r'Total', line):
            total = line
        else:
            items.append(line)

    # Get Name, quantity and cost 
    all_items = {}
    for item in items:
        details = item.split()
        quantity_name = details[0]
        if len(quantity_name.split('x')) > 1:
            quantity = quantity_name.split('x')[0]
            name = quantity_name.split('x')[1]
        cost = details[-1]
        all_items[name] = {'quantity':quantity, 'cost':cost}
    
    if 'total' in line:
        total = total.split('CHF')[-1]
        receipt_ocr['total'] = total


    # Store the results in the dict
    receipt_ocr['items'] = all_items

    return receipt_ocr

# Unit testing
if __name__ == '__main__':
    img_file = 'imgs/demo.png'
    response = json_response(img_file)
    print(response)