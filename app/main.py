from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI(title="Luna API", version="0.1.0")

app.include_router(api_router, prefix="/v1")


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "UP"}
