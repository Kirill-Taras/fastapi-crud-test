from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from config.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    status = Column(String(20), nullable=False, default="Не начата")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
