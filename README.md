# FastAPI CRUD Test

Тестовое задание: реализация CRUD API с использованием **FastAPI**, **Pydantic** и **PostgreSQL**.  
Приложение поддерживает работу с сущностями (создание, чтение, обновление, удаление).

---

## 📂 Структура проекта

fastapi-crud-test/ # Корневая директория проекта
├── .venv/ # Виртуальное окружение (не коммитится)
├── config/ # Конфигурация приложения
│ ├── init.py
│ └── (config.py, settings.py)
├── models/ # ORM-модели (SQLAlchemy)
│ ├── init.py
│ └── (item.py, user.py)
├── routers/ # Эндпоинты API (роутеры FastAPI)
│ ├── init.py
│ └── (items.py, users.py)
├── schemas/ # Pydantic-схемы (валидация, сериализация)
│ ├── init.py
│ └── (item.py, user.py)
├── services/ # Бизнес-логика (сервисный слой)
│ ├── init.py
│ └── (item_service.py)
├── .gitignore # Игнорируемые файлы для Git
├── main.py # Точка входа (создание FastAPI-приложения)
├── README.md # Описание проекта
└── requirements.txt # Зависимости Python


---

## 🚀 Запуск проекта

### 1. Клонирование репозитория
```bash
git clone https://github.com/YOUR_USERNAME/fastapi-crud-test.git
cd fastapi-crud-test
2. Установка зависимостей

Создать виртуальное окружение и активировать:

python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate   # Linux/Mac


Установить пакеты:

pip install -r requirements.txt

3. Запуск приложения
uvicorn main:app --reload


API будет доступно по адресу:

http://127.0.0.1:8000/docs

🛠 Технологии

FastAPI

Pydantic

SQLAlchemy

PostgreSQL

Alembic
 (миграции)

📌 Задачи (MVP)

 Настроить подключение к Postgres

 Определить модели и схемы

 Реализовать CRUD-операции

 Добавить эндпоинты

 Подключить Docker/Docker Compose

 Обновить документацию