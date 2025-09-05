from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.task import Task
from schemas.task import TaskCreate, TaskUpdate


async def create_task(db: AsyncSession, task_create: TaskCreate) -> Task:
    """
    Создание новой задачи.
    :param db: сессия базы данных
    :param task_create: Pydantic-схема TaskCreate
    :return: созданная Task
    """
    task = Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)  # чтобы получить id и дату создания
    return task


async def get_task(db: AsyncSession, task_id: int) -> Optional[Task]:
    """
    Получение задачи по ID.
    :param db: сессия базы данных
    :param task_id: идентификатор задачи
    :return: Task или None, если не найдено
    """
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalars().first()


async def get_all_tasks(
    db: AsyncSession, limit: int = 10, search: Optional[str] = None
) -> List[Task]:
    """
    Получение всех задач с фильтрацией.
    :param db: сессия базы данных
    :param limit: сколько записей вернуть
    :param search: поиск по названию
    """
    query = select(Task)
    if search:
        query = query.where(Task.title.ilike(f"%{search}%"))
    result = await db.execute(query.limit(limit))
    tasks: List[Task] = list(result.scalars().all())
    return tasks


async def update_task(
    db: AsyncSession, task_id: int, task_update: TaskUpdate
) -> Optional[Task]:
    """
    Обновление задачи по ID.
    :param db: сессия базы данных
    :param task_id: идентификатор задачи
    :param task_update: Pydantic-схема TaskUpdate
    :return: обновлённая Task или None, если не найдено
    """
    task = await get_task(db, task_id)
    if not task:
        return None
    for field, value in task_update.dict(exclude_unset=True).items():
        setattr(task, field, value)
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def delete_task(db: AsyncSession, task_id: int) -> bool:
    """
    Удаление задачи по ID.
    :param db: сессия базы данных
    :param task_id: идентификатор задачи
    :return: True, если удалено, False если задача не найдена
    """
    task = await get_task(db, task_id)
    if not task:
        return False
    await db.delete(task)
    await db.commit()
    return True
