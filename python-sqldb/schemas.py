# schemas.py
from pydantic import BaseModel
from datetime import date
 
class BookBase(BaseModel):
    title: str
    author: str
    published_date: date
 
class BookCreate(BookBase):
    pass
 
class Book(BookBase):
    id: int
 
    class Config:
        orm_mode = True