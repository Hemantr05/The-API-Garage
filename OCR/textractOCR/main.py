import logging
from fastapi import FastAPI, Form, FileUpload, File, HTTPException
logging.basicConfig(filename='compile.log', level=logging.DEBUG)

from utils import *
from textract_forms import *

app = FastAPI()

image_extensions = ['png', 'jpg', 'jpeg']
pdf_extensions = ['pdf', 'PDF']


@app.get('/')
async def get():
    return {"Status": "Ok"}

@app.get('/')
async def textractOCR(file: FileUpload = File(...),
                    aws_access_key_id: str = Form(...),
                    aws_secret_access_key: str = Form(...),
                    region_name: str = Form(...)):

    file_name = save_upload_file_tmp(file)
    logging.info('File uploaded successfully')
    name, extn = file_name.split('.')
    response = dict()

    if extn in image_extensions:
        logging.info('Detected file type as image')
        forms = get_forms_from_image(file_name, access_key_id, secret_access_key, region_name)
        response['form'] = forms
        logging.info('Forms successfully extracted from file')
        return response

    elif extn in pdf_extensions:
        logging.info('Detected file type as pdf')
        forms = get_forms_from_pdf(file_name, access_key_id, secret_access_key, region_name)
        response['form'] = forms
        logging.info('Forms successfully extracted from file')
        return response

    else:
        raise HTTPException(status_code=404, detail="Invalid File Type")
