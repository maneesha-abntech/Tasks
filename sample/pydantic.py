from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class itemA(BaseModel):
    name:str
    description:str
class itemB(BaseModel):
    price:float
    quantity:int
@app.post("/items/")
def create_items(item_a:itemA,item_b:itemB):
    print(item_a)
    return{"item_a":item_a,"item_b":item_b}