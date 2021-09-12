from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse

from utils import prep_image, color_analysis


app = FastAPI()


@app.get("/")
async def get():
    return {"response": "Ok"}

@app.post("/")
async def analyze(file: UploadFile = File(...)):

    filename = save_upload_file_tmp(file, "uploads")

    # Check for file type (image or video)

    # For image
    preprocess_image = prep_image(filename)
    color_analysis(preprocess)
    # return StreamingResponse(predicted, media_type="image/png")


    # TODO: read and return predicted video file .
    # For video


    # Download or send response as image or video with predictions
