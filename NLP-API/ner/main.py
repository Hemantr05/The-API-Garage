from fastapi import FastAPI, Form
from utils import bert_coll03

app = FastAPI()

app.get("/")
async def get():
	return {"Status", "Ok"}
	
app.post("/")
async def ner(text: str = Form(...)):
	response = bert_coll03(text)
	return response
