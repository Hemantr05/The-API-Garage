from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse

from utils import prep_image, color_analysis, save_upload_file_tmp


app = FastAPI()


@app.get("/")
async def get():
    return {"response": "Ok"}

@app.post("/")
async def analyze(file: UploadFile = File(...)):

    filename = save_upload_file_tmp(file, "uploads")

    preprocess_image = prep_image(filename)
    colors = color_analysis(preprocess)
    return colors

    # Download or send response as image or video with predictions
