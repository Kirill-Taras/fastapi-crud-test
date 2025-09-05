from fastapi import FastAPI

from routers import task


def create_app() -> FastAPI:
    """
    Фабрика приложения FastAPI.
    Возвращает экземпляр приложения с подключенными роутерами.
    """
    app = FastAPI(title="FastAPI CRUD Test", version="1.0.0")

    app.include_router(task.router)

    return app


app = create_app()
