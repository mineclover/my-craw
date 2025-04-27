from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .database import SessionLocal, init_db
from .models import RequestLog

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    # 종료 시 실행할 코드가 있다면 여기에 작성

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "Hello, FastAPI!"})

@app.middleware("http")
async def log_request(request: Request, call_next):
    response = await call_next(request)
    db = SessionLocal()
    try:
        log = RequestLog(method=request.method, url=str(request.url))
        db.add(log)
        db.commit()
    finally:
        db.close()
    return response 