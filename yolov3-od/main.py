import cv2
import os
import shutil
from pathlib import Path
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse

from utils import (predictImage, 
                    predictVideo, 
                    testFunction,
                    save_upload_file_tmp
                    )


app = FastAPI()


@app.get("/")
async def get():
    return {"response": "Ok"}

@app.post("/")
async def predict(file: UploadFile = File(...)):

    # with open("input.jpg", "wb") as buffer:
    #     shutil.copyfileobj(file.file, buffer)
    # filename = Path(buffer.name)
    # filename = filename.name
    # filename = buffer.name

    filename = save_upload_file_tmp(file, "uploads")

    # img_bytes = testFunction(filename)
    # return StreamingResponse(img_bytes, media_type="image/png")

    # Check for file type (image or video)
    # print(filename)
    predicted = predictImage(filename)
    return StreamingResponse(predicted, media_type="image/png")


    
    # Download or send response as image or video with predictions