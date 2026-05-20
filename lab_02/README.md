# Система бронирования отелей

## Описание
Система позволяет пользователям искать отели и бронировать номера.

## 1. Роли
- Пользователь
- Администратор

## 2. Внешние системы
- Платежная система
- e-mail сервис

## 3. Основные сценарии
- Пользователь:
  - регистрация
  - вход
  - поиск отелей
  - бронирование
  - отмена бронирования
  - просмотр своих бронирований
  - просмотр профиля
- Админ:
  - создание отеля
  - просмотр списка отелей

## 4. Перечень container
<!-- Используется микросервисная архитектура, состаящая из контейнеров:
- API
- Auth Service
- User Service
- Hotel Service
- Booking Service
- Notification Service
- Database (PostgreSQL) -->

| Контейнер            | Назначение                   | Технология           | Протоколы взаимодействия |
| -------------------- | ---------------------------- | -------------------- | ------------------------ |
| API Gateway          | Точка входа                  | REST API             | HTTPS / REST             |
| Auth Service         | Авторизация и аутентификация | Spring Boot REST API | HTTPS / REST, JWT        |
| User Service         | Управление пользователями    | Spring Boot REST API | HTTPS / REST, JDBC       |
| Hotel Service        | Управление отелями           | Spring Boot REST API | HTTPS / REST, JDBC       |
| Booking Service      | Управление бронированиями    | Spring Boot REST API | HTTPS / REST, JDBC       |
| Notification Service | Email-уведомления            | Spring Boot          | SMTP / REST              |
| PostgreSQL           | Основная база данных         | PostgreSQL           | JDBC                     |



Основные сценарии взаимодействия
1. Создание пользователя
Последовательность
- Пользователь отправляет форму регистрации
- Web Application вызывает API Gateway
- API Gateway перенаправляет запрос в User Service
- User Service сохраняет пользователя в PostgreSQL
- User Service возвращает результат

2. Поиск отелей по городу
Последовательность
- Пользователь вводит город
- Web Application отправляет запрос
- API Gateway вызывает Hotel Service
- Hotel Service получает данные из PostgreSQL
- Список отелей возвращается пользователю

3. Создание бронирования
Последовательность
- Пользователь выбирает отель
- Web Application отправляет запрос на бронирование
- API Gateway вызывает Booking Service
- Booking Service проверяет доступность отеля через Hotel Service
- Booking Service сохраняет бронь в PostgreSQL
- Booking Service выполняет оплату через Payment System
- Notification Service получает событие
- Notification Service отправляет email пользователю

4. Получение бронирований пользователя
Последовательность
- Пользователь открывает список бронирований
- Web Application вызывает Booking Service
- Booking Service читает данные из PostgreSQL
- Результат возвращается пользователю
5. Отмена бронирования
Последовательность
- Пользователь отменяет бронирование
- Booking Service обновляет статус брони
- Booking Service отправляет событие BookingCancelled
- Notification Service отправляет email