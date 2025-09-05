FROM python:3.11-slim

# Установим рабочую директорию
WORKDIR /app

# Установим зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопируем проект
COPY . .

# Команда запуска
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
