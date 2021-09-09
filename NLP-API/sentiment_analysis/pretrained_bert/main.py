from fastapi import FastAPI, Form
from analyzer import *

app = FastAPI()

@app.get("/")
async def get_request():
	
	# TODO: To retrieve sentiment for a given id or sentence from the database
	return {"status": "Ok"}
	
	
@app.post("/")
async def phrase_sentiment(text: str = Form(...)):
	sentiment, score = simple_analyzer(text)
	
	# TODO: To store into existing database
	return {"text": text, "sentiment": sentiment, "score": score}
	
	
