from fastapi import APIRouter
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user_router = APIRouter(prefix='/users', tags=['Users'])

@user_router.get("/{user_id}")
async def get_user(user_id: int):
    return {"message": f"Hello, your id is {user_id}"}

@user_router.post("/")
async def create_user(user: User):
    return {"message": f"Hello {user.name}, you are {user.age} years old"}