from fastapi import FastAPI
from app.database import engine, Base
from app.routers.word import word_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(word_router)

@app.get("/")
async def home():
    return {"Hello": "World!"}
