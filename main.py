from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel 


class Package(BaseModel):
    name: str
    number: int
    description : str 

    

app = FastAPI()


@app.get('/')
async def hello_world():
    return {"Hello": "World"}


# @app.get("/component/{component_id}") #path parameter
# async def get_component(component_id: int):
#     return {"component_id": component_id}

# @app.get("/component/") 
# async def read_component(number: int, text: Optional[str]): #queary parameter
#     return {"number": number , "text" : text}

@app.post("/package/{priority}")
async def make_package( priority: int, package: Package ,value : bool):
    return {"priority": priority , **package.dict(), "value": value}
