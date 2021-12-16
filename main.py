# Python
from typing import Optional
from datetime import datetime
from enum import Enum

# Pydantinc
from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.networks import EmailStr

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path


app = FastAPI()

# Models
class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"


class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=100
        )
    state: str = Field(
        ...,
        min_length=1,
        max_length=100
        )
    country: str = Field(
        ...,
        min_length=1,
        max_length=100
        )


class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    age: int = Field(
        ...,
        gt=0,
        le=120
        )
    birthday: datetime
    hair_color: Optional[HairColor] = Field(
            default=None
        )
    is_married: Optional[bool] = Field(
        default=None,
        )
    email: EmailStr = Field(
        ...,
    )

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Carlos",
                "last_name": "La Fuente",
                "age": 25,
                "birthday": datetime.now(),
                "hair_color": HairColor.blonde,
                "is_married": False,
                "email": "user@example.com"
            }
        }


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
        description="This is the user name. It's between 1 and 50 characters.",
        example="Carlos"
        ), 
    age: int = Query(
        ..., 
        title="User age", 
        description="This is the user age. It's a required query parameter.",
        example=25
        )
    ):
    return { "name": name, "age": age }

# Validations: Path parameters
@app.get("/user/detail/{user_id}")
def get_user_detail(
    user_id: int = Path(
        ..., 
        gt=0,
        title="User ID",
        description="This is the user ID. It's greater than 0.",
        example=123
        )
    ):
    return { "name": "Carlos", "age": 25, "id": user_id }


# Validations: Request Body 
@app.put("/user/{user_id}")
def update_user(
        user_id: int = Path(
        ..., 
        gt=0,
        title="User ID",
        description="This is the user ID. It's greater than 0.",
        example=123
        ),
        person: Person = Body(...),
        location: Location = Body(...)
    ):
    # result = person.dict()
    # result.update(location.dict())

    # person.dict() & location.dict()
    return person