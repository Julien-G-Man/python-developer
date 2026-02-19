from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

@app.post("/")  
def root(item: Item):
    name = item.name
    return {"message": f"We have {name}"}