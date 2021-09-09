from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse

from utils import (predictImage, 
                    predictVideo, 
                    save_upload_file_tmp)


app = FastAPI()


@app.get("/")
async def get():
    return {"response": "Ok"}

@app.post("/")
async def predict(file: UploadFile = File(...)):

    filename = save_upload_file_tmp(file, "uploads")

    # Check for file type (image or video)

    # For image
    predicted = await predictImage(filename)
    return StreamingResponse(predicted, media_type="image/png")


    # TODO: read and return predicted video file .
    # For video

    
    # Download or send response as image or video with predictions