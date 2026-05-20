# Hotel Booking System (REST API + Docker + PostgreSQL)

##  Описание проекта

Учебный проект системы бронирования отелей, реализованный в рамках курса **«Архитектура программных систем»**.

Система позволяет:
- регистрировать и авторизовать пользователей (JWT)
- управлять пользователями
- создавать и просматривать отели
- выполнять бронирование отелей
- отменять бронирования
- выполнять поиск пользователей и отелей

---

## Архитектура

Проект построен по слоистой архитектуре:
Controllers → Services → Repositories → Database


Каждый слой отвечает за свою область ответственности:
- **Controllers** — обработка HTTP запросов
- **Services** — бизнес-логика
- **Repositories** — работа с БД
- **Database** — PostgreSQL

---

## Сущности системы

- **User** — пользователь системы
- **Hotel** — отель
- **Booking** — бронирование

---

## Технологии

- Python 3.11
- FastAPI
- PostgreSQL 16
- psycopg2
- JWT (python-jose)
- Docker / Docker Compose

---

##  Запуск проекта

docker compose build --no-cache
docker compose up

http://localhost:8000/docs


# Структура базы данных
## Таблица users
- id (PK)
- login (UNIQUE)
- password
- first_name
- last_name
## Таблица hotels
- id (PK)
- name
- city
- address
- description
## Таблица bookings
- id (PK)
- user_id
- hotel_id
- check_in
- check_out

# Индексы

Для оптимизации запросов добавлены индексы:

- users(login) — быстрый поиск пользователя
- hotels(city) — поиск отелей по городу
- bookings(user_id) — получение бронирований пользователя
- bookings(hotel_id) — ускорение JOIN запросов