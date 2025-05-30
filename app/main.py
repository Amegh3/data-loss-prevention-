import uvicorn
from fastapi import FastAPI
from app.api.endpoints import router
from app.db.models import Base
from app.db.session import engine

app = FastAPI(title="Advanced DLP System")

app.include_router(router)

@app.on_event("startup")
async def on_startup():
    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
