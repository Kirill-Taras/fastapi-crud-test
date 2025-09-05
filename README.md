# 💻FastAPI CRUD Test

Простой CRUD-проект на FastAPI с асинхронным доступом к PostgreSQL.  
Позволяет создавать, получать, обновлять и удалять задачи через REST API.  

## 🐾Стек технологий

- **Python**
- **FastAPI** – веб-фреймворк для API
- **SQLAlchemy** – ORM для работы с базой данных
- **PostgreSQL** – реляционная база данных
- **asyncpg** – асинхронный драйвер для PostgreSQL
- **Docker & Docker Compose** – контейнеризация приложения и базы данных
- **Uvicorn** – ASGI сервер для запуска FastAPI
- **Pydantic** – валидация и сериализация данных
- **Swagger / OpenAPI** – документация API

## 📂Структура проекта

```text
fastapi-crud-test/
├── main.py           # Точка входа приложения FastAPI
├── routers/          # Роутеры (эндпоинты API)
│   └── task.py
├── models/           # Модель задачи
│   └── task.py
├── schemas/          # Pydantic-схемы для валидации данных
│   └── task.py
├── services/         # Логика работы с базой (CRUD-функции)
│   └── task_service.py
├── config/           # Настройки и подключение к БД
│   ├── db.py
│   └── settings.py
├── .env                  # Переменные окружения (БД, порты и т.д.)
├── requirements.txt      # Зависимости Python
├── Dockerfile            # Инструкция для сборки Docker-образа
├── docker-compose.yml    # Сборка приложения + БД через Docker
└── README.md             # Документация проекта
```
---

## 🚀 Запуск проекта

### 1. Клонируем репозиторий

```bash
# клонируем репозиторий
git clone https://github.com/Kirill-Taras/fastapi-crud-test.git
# переходим в папку проекта
cd fastapi-crud-test
```

### 2. Создаем виртуальное окружение и активируем его
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Устанавливаем зависимости
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
### 4. Настраиваем переменные окружения
```bash
Создайте файл .env в корне проекта и заполните его:

POSTGRES_DB=name_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=pass
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

DATABASE_URL=postgresql+asyncpg://postgres:pass@localhost:5432/name_db

```
⚠️ Для работы проекта необходима локальная или удалённая PostgreSQL база.

### 5. Создаем базу данных fastapi_db в PostgreSQL (если еще нет):
```bash
CREATE DATABASE fastapi_db;
```
### 6. Запуск приложения:
```bash
uvicorn main:app --reload
```

Сервер будет доступен по адресу: http://127.0.0.1:8000/tasks/

### 7. Доступ к документации
```bash
Swagger: http://127.0.0.1:8000/docs/
```

## 🐳 Запуск через Docker

### 1. Клонируем репозиторий
```bash
# клонируем репозиторий
git clone https://github.com/Kirill-Taras/fastapi-crud-test.git
# переходим в папку проекта
cd fastapi-crud-test
```

### 2. Настраиваем переменные окружения
Создайте файл .env в корне проекта и заполните его:
```bas
POSTGRES_DB=fastapi_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=pass
POSTGRES_HOST=db
POSTGRES_PORT=5432

DATABASE_URL=postgresql+asyncpg://postgres:pass@db:5432/fastapi_db
```

### 3. Сборка и запуск контейнеров:

```bash
docker compose up -d --build
```

### 4. Проверяем работу приложения:

```bash
Swagger UI: http://127.0.0.1:8000/docs

Эндпоинты CRUD: /tasks/, /tasks/{id}
```

### 5. Просмотр логов контейнеров:

```bash
docker compose logs -f web
docker compose logs -f db
```

### 6. Остановка и удаление контейнеров:

```bash
docker compose down
```

## 🕹️ Эндпоинты

| Метод | URL                  | Описание                              |
|-------|--------------------|---------------------------------------|
| GET   | /tasks/             | Получить список всех задач            |
| GET   | /tasks/{id}         | Получить задачу по ID                 |
| POST  | /tasks/             | Создать новую задачу                   |
| PUT   | /tasks/{id}         | Обновить задачу по ID                  |
| DELETE| /tasks/{id}         | Удалить задачу по ID                   |

### 🧑‍💼Разработчик: Тарасов Кирилл