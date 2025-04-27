from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.database import init_db
from app.api.todo import router as todo_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(todo_router, prefix="/todos", tags=["todos"])

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "Hello, FastAPI!"})

# 요청 로그 미들웨어 예시 (원하면 유지)
# from app.core.database import SessionLocal
# from app.models.request_log import RequestLog
# @app.middleware("http")
# async def log_request(request: Request, call_next):
#     response = await call_next(request)
#     db = SessionLocal()
#     try:
#         log = RequestLog(method=request.method, url=str(request.url))
#         db.add(log)
#         db.commit()
#     finally:
#         db.close()
#     return response 