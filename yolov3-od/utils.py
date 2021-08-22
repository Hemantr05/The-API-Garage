import io
import os
import cv2
import shutil
import matplotlib.pyplot as plt

from pathlib import Path
from tempfile import NamedTemporaryFile
from fastapi import FastAPI, File, UploadFile


def predictImage(imageDir):
    """Returns image with predictions"""
    os.system("cd darknet && ./darknet detect cfg/yolov3.cfg yolov3.weights {}".format(imageDir))
    image = cv2.imread("darknet/predictions.jpg")
    height, width = image.shape[:2]
    resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)
    bgr2rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    res, im_png = cv2.imencode(".png", bgr2rgb)
    img_bytes = io.BytesIO(im_png.tobytes())
    return img_bytes 

def predictVideo(videoDir):
    """Returns video with predictions"""
    os.system(""" cd darknet && ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights \
    -dont_show {} -i 0 -out_filename output.avi
    """.format(videoDir))


def testFunction(img):
    image = cv2.imread(img)
    res, im_png = cv2.imencode(".png", image)
    img_bytes = io.BytesIO(im_png.tobytes())
    return img_bytes


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
    return tmp_path