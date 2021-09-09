from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from utils import save_upload_file_tmp, correct, train2

app = FastAPI()

@app.get("/")
async def test():
    return {"Response": "Ok"}

@app.post("/")
async def correction(file: UploadFile = File(...)):
    file_ = save_upload_file_tmp(file)

    spell_correct_text = correct(file_)

    with open("results.txt", "w+") as f:
        f.write(spell_correct_text)

    # TODO: Return file with corrected spellings
    return StreamingResponse()


@app.post("/train")
async def train(file: UploadFile = File(...),
                trainFile: UploadFile = File(...)):

    file_ = save_upload_file_tmp(file)
    train_file = save_upload_file_tmp(trainFile)

    corrected_text = train2(file_, train_file)

    with open("result.txt", "w+") as f:
        f.write(corrected_text)

    # TODO: Return file with corrected spellings
    return StreamingResponse()