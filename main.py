import uvicorn
from fastapi import FastAPI
from config.db import engine, Base
from routers import task

app = FastAPI(title="FastAPI CRUD Test", version="1.0.0")
app.include_router(task.router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Таблицы созданы и база готова!")


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()
    print("Соединение с базой закрыто.")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

