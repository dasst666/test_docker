from fastapi import FastAPI
from api.users import user_router
from fastapi import APIRouter

app = FastAPI()

v1_router = APIRouter(prefix='/v1', tags=['v1'])
v2_router = APIRouter(prefix='/v2', tags=['v2'])

v1_router.include_router(user_router)
v2_router.include_router(user_router)


app.include_router(v1_router)
app.include_router(v2_router)

@app.get("/")
async def root(name: str):
    return {"message": f"Hello {name}"}

