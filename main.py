# Python
from typing import Optional
from datetime import datetime

# Pydantinc
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body


app = FastAPI()

# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    birthday: datetime
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

# Path Operations
@app.get("/")
def home():
    return { "data": "Hello World!" }

# Request and Response Body
@app.post("/user")
def create_user(person: Person = Body(...)):

    return person
