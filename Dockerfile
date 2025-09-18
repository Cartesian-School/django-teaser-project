FROM python:3.13-trixie

# Отключает запись pyc файлов и буферизацию вывода
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей (requirements.txt должен быть в корне проекта)
COPY requirements.txt /app/requirements.txt

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app

# Открываем порт для доступа к приложению
EXPOSE 8000

# Команда для запуска сервера разработки Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
