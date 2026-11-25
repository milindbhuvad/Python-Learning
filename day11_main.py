
from fastapi import FastAPI

from day11_auth import router as auth_router

app = FastAPI(title="Authentication API")
app.include_router(auth_router)
