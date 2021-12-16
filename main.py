# Python
from typing import Optional
from datetime import datetime

# Pydantinc
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path


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

# Validations: Query parameters
@app.get("/user/detail")
def get_user_detail(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="User name",
        description="This is the user name. It's between 1 and 50 characters."
        ), 
    age: int = Query(
        ..., 
        title="User age", 
        description="This is the user age. It's a required query parameter."
        )
    ):
    return { "name": name, "age": age }

# Validations: Query parameters
@app.get("/user/detail/{user_id}")
def get_user_detail(
    user_id: int = Path(
        ..., 
        gt=0,
        title="User ID",
        description="This is the user ID. It's greater than 0."
        )
    ):
    return { "name": "Carlos", "age": 25, "id": user_id }
