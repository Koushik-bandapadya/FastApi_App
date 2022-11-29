from fastapi import FastAPI, Form 

app = FastAPI()


@app.get("/")
async def hello():
    return {"Hello": "World"}

@app.post("/language/")
async def langauge(name: str = Form(), type: str = Form()):
    return {"name": name, "type": type}



@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username , "password" : password }