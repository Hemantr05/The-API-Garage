from fastapi import FastAPI, Form, FileUpload, File, HTTPException

from utils import *

app = FastAPI()

image_extensions = ['png', 'jpg', 'jpeg']
pdf_extensions = ['pdf', 'PDF']


@app.get('/')
async def get():
    return {"Status": "Ok"}

@app.post('/')
async def UniversalSentenceEmbedding(sentence: str = Form(...)):
    embedding_response = USE(sentence)
    return embedding_response
    