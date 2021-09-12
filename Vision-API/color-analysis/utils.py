import argparse
import cv2
from collections import Counter
# import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from fastapi import UploadFile
from pathlib import Path
import shutil
from tempfile import NamedTemporaryFile
import json

def save_upload_file_tmp(upload_file: UploadFile, dest: str):
    """Returns temporary path for uploaded file"""
    try:
        dest = Path(dest)
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()

def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color

def prep_image(raw_img):
    modified_img = cv2.resize(raw_img, (900, 600), interpolation = cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3)
    return modified_img

def color_analysis(img, colors):
    color_label = dict()
    clf = KMeans(n_clusters = 5)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
    hex_colors = [str(i) for i in hex_colors]
    
    for color in hex_colors:
        label = colors[color]
        color_label[color] = label
    return color_label

    
    # plt.figure(figsize = (12, 8))
    # plt.pie(counts.values(), labels = hex_colors, colors = hex_colors, autopct='%1.1f%%')
    # plt.savefig("color_analysis_report.png")
    # print(hex_colors)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, required=True, help="Path to image")
    args = parser.parse_args()

    with open('./color.json') as f:
        colors = json.load(f)

    image = cv2.imread(args.image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    modified_image = prep_image(image)
    color_analysis(modified_image, colors)
