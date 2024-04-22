"""from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
"""
#post method
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class itemA(BaseModel):
    name:str
    description:str
@app.post("/items")
def create_items(item_a:itemA):
    print(item_a)
    return{"item_a":item_a}







