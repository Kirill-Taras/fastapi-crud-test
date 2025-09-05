from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from config.db import get_db
from models.task import Task as TaskModel
from schemas.task import Task, TaskCreate, TaskUpdate
from services.task_service import (
    create_task,
    delete_task,
    get_all_tasks,
    get_task,
    update_task,
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=List[Task])
async def list_tasks(
    limit: int = Query(10, description="Максимальное количество задач"),
    search: Optional[str] = Query(None, description="Поиск по названию"),
    db: AsyncSession = Depends(get_db),
) -> List[TaskModel]:
    """
    Получить список задач с поддержкой поиска и лимита.
    """
    return await get_all_tasks(db, limit=limit, search=search)


@router.get("/{task_id}", response_model=Task)
async def get_task_by_id(task_id: int, db: AsyncSession = Depends(get_db)) -> TaskModel:
    """
    Получить задачу по ID.
    """
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task


@router.post("/", response_model=Task, status_code=201)
async def create_new_task(
    task_create: TaskCreate, db: AsyncSession = Depends(get_db)
) -> TaskModel:
    """
    Создать новую задачу.
    """
    return await create_task(db, task_create)


@router.put("/{task_id}", response_model=Task)
async def update_existing_task(
    task_id: int, task_update: TaskUpdate, db: AsyncSession = Depends(get_db)
) -> TaskModel:
    """
    Обновить задачу по ID.
    """
    task = await update_task(db, task_id, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task


@router.delete("/{task_id}", status_code=204)
async def delete_existing_task(
    task_id: int, db: AsyncSession = Depends(get_db)
) -> None:
    """
    Удалить задачу по ID.
    """
    success = await delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return None
