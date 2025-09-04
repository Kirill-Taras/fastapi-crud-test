from fastapi import FastAPI

def create_app() -> FastAPI:
    """
    Фабрика приложения FastAPI.
    Возвращает экземпляр приложения с подключенными роутерами.
    """
    app = FastAPI(title="FastAPI CRUD Test", version="1.0.0")
    return app

app = create_app()
