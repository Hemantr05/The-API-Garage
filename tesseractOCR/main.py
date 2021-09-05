from tess_ocr import json_response
from utils import save_upload_file_tmp
from pdf2image import convert_from_path
from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI()

IMG_EXTN = ['.png', '.jpg', '.jpeg']

@app.get('/')
def get():
    return {"Status": "Ok"}

@app.post('/')
async def get_ocr(file: UploadFile = File(...)):
    """OCR for input pdf/image file"""
    filename = save_upload_file_tmp(file, ".")
    stem, extn = filename.stem, filename.suffix

    if extn in IMG_EXTN:
        ocr = await json_response(filename)
        return ocr
    elif extn == '.pdf':
        images = convert_from_path(filename)
        pdf_response = []
        for idx, img in enumerate(images):
            ocr = await json_response(img)
            ocr['page_no'] = idx+1
            pdf_responsea.append(ocr)
        return pdf_response
    else:
        raise HTTPException(status_code=404, detail="Invalid file type")

