from fastapi import FastAPI, Form

app = FastAPI()

app.get("/")
async def get():
	return {"Status", "Ok"}
	
app.post("/")
async def allAPIS():
    pass
