from fastapi import FastAPI
from app.routers import compliance
import uvicorn

app = FastAPI()

app.include_router(compliance.router)

if __name__ == "__main__":
    uvicorn(host="127.0.0.1",port =8000)


