# Hotel Booking API

REST API сервис для системы бронирования отелей.

Проект реализован на:
- FastAPI
- JWT Authentication
- Docker
- Swagger/OpenAPI

---

# Функциональность

## Пользователи
- Регистрация пользователя
- Авторизация пользователя
- Поиск пользователя по логину
- Поиск пользователей по имени/фамилии

## Отели
- Создание отеля
- Получение списка отелей
- Поиск отелей по городу

## Бронирования
- Создание бронирования
- Получение бронирований пользователя
- Отмена бронирования

---

# Технологии

- Python 3.11
- FastAPI
- JWT
- Docker
- Pytest

---

# Структура проекта

```text
src/
│
├── api/
├── dto/
├── model/
├── security/
├── services/
│
└── main.py
tests/
```

Запуск проекта локально
Установка зависимостей
pip install -r requirements.txt
Запуск приложения
uvicorn src.main:app --reload

После запуска приложение доступно:

Swagger UI
http://localhost:8000/docs

OpenAPI
http://localhost:8000/openapi.json

# Docker
- Сборка контейнера
```docker compose build```
- Запуск контейнера
```docker compose up```
- Остановка контейнера
CTRL + C

# Тесты
Запуск тестов локально
```python -m pytest ```

# Основные endpoints
- Authentication

Регистрация POST /auth/register

Авторизация POST /auth/login

- Hotels

Создание отеля POST /hotels/

Получение списка отелей GET /hotels/

Поиск по городу GET /hotels/search?city=Amsterdam

- Bookings

Создание бронирования POST /bookings/

Получение бронирований пользователя GET /bookings/{user_id}

Отмена бронирования DELETE /bookings/{booking_id}

- Аутентификация

Для защищённых endpoints используется JWT Bearer Token.

Токен можно получить через:

POST /auth/login