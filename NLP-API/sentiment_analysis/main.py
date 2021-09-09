from fastapi import FastAPI, Form
from .pretrained_bert import *

app = FastAPI()

app.get("/")
async def get():
	return {"Status", "Ok"}
	
app.post("/")
async def sentiment(text: str = Form(...)):
	sentiment, score = analyzer.simple_analyzer(text)
	return {"text": text, "sentiment": sentiment, "score": score}
