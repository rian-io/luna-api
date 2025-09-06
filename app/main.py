from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI(title="Luna API", version="0.1.0")


app.include_router(api_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
