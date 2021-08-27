from utils import save_upload_file_tmp
from pdf2image import convert_from_path
from utils import detect_layout_from_img
from fastapi import FastAPI, File, UploadFile, HTTPException, Form

IMG_EXTN = ['.png', '.jpg', '.jpeg']
PDF_EXTN = ['.pdf', '.PDF']
app = FastAPI()


@app.get('/')
def get():
    return {"Status": "Ok"}

@app.post('/')
async def page_layout(file: UploadFile = File(...), threshold: float = Form(...)):
    """page layout pdf/image file"""
    filename = save_upload_file_tmp(file, ".")
    stem, extn = filename.stem, filename.suffix

    if extn in IMG_EXTN:
        layout = await detect_layout_from_img(filename, threshold)
        return layout

    elif extn in PDF_EXTN:
        images = convert_from_path(filename, fmt='.png')
        all_pages = []
        for pno, img in enumerate(images):
            layout = await detect_layout_from_img(img, threshold)
            layout['page_no'] = pno+1
            layout['page_width'], layout['page_height'] = img.width, img.height
            all_pages.append(layout)
        return all_pages

    else:
        raise HTTPException(status_code=404, detail="Invalid File Type")

