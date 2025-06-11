from fastapi import FastAPI
from app.api import router

app = FastAPI()

app.include_router(router)


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 如果不确定，先写 ["*"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)