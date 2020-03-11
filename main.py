from fastapi import FastAPI, Response, Request

from src.api import routers
from db.session import SessionLocal, engine

app = FastAPI(
    title="My first blog FastAPI",
    description="Author - DJWOMS",
    version="0.5",
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(routers.api_router)
