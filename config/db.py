from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import text
from config.settings import settings

class Base(DeclarativeBase):
    """Базовый класс для моделей (SQLAlchemy ORM)."""
    pass

engine = create_async_engine(settings.database_url, echo=False, pool_pre_ping=True)

SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def ping_db(session: AsyncSession) -> bool:
    """
    Проверка подключения к базе.
    Возвращает True, если SELECT 1 успешно выполнился.
    """
    try:
        result = await session.execute(text("SELECT 1"))
        return result.scalar() == 1
    except Exception:
        return False