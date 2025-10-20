from fastapi import FastAPI
from api.users import user_router
from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import Response, FileResponse, JSONResponse

app = FastAPI()

v1_router = APIRouter(prefix='/v1', tags=['v1'])
v2_router = APIRouter(prefix='/v2', tags=['v2'])

v1_router.include_router(user_router)
v2_router.include_router(user_router)


app.include_router(v1_router)
app.include_router(v2_router)

class ResponseExample(BaseModel):
    message: str
    message3: str | None = None


@app.get("/", response_model=ResponseExample)
async def root(response: Response):
    response.set_cookie(key="fakesession", value="fake-ccokie-session-value")
    response.headers["Test_header"] = "testtttt"
    return {"message": "test"}

