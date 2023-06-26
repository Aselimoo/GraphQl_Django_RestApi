# Указываем базовый образ, основанный на Python
FROM python:3.9

# Устанавливаем переменную окружения PYTHONUNBUFFERED в значение 1
# Это гарантирует, что вывод Python будет отправляться прямо в терминал без буферизации
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы requirements.txt в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости, перечисленные в файле requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Запускаем команду для выполнения миграций Django и сбора статических файлов
RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# Открываем порт, который будет использоваться вашим Django приложением
EXPOSE 8000

# Запускаем сервер Django при старте контейнера
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]