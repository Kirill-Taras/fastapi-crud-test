from fastapi import FastAPI

from config.db import ping_db, SessionLocal


def create_app() -> FastAPI:
    """
    Фабрика приложения FastAPI.
    Возвращает экземпляр приложения с подключенными роутерами.
    """
    app = FastAPI(title="FastAPI CRUD Test", version="1.0.0")

    @app.on_event("startup")

    async def startup():
        async with SessionLocal() as session:
            await ping_db(session)

    return app

app = create_app()
