# Hotel Booking API — Event-Driven Architecture

В рамках данного задания была реализована Event-Driven архитектура для системы бронирования отелей.Основной REST API построен на FastAPI. Для обмена событиями между компонентами системы был подключен RabbitMQ. Реализованы producer и consumer сервисы, позволяющие публиковать и обрабатывать события асинхронно.

Дополнительно в проекте уже используются:


## Система построена по Event-Driven подходу:

- REST API принимает запросы от клиента
- Service layer выполняет бизнес-логику
- После выполнения операций публикуются события в RabbitMQ
- Consumer подписывается на события и асинхронно их обрабатывает

Используется exchange типа topic, что позволяет гибко маршрутизировать события по routing keys.

## Реализованные события

В проекте реализована публикация событий, связанных с:

- hotel.get
- hotel.created
- booking.created
- booking.canceled 

Каждое событие публикуется producer сервисом в exchange hotel_events.

## Producer

Producer отвечает за отправку событий в RabbitMQ. Используется:

```
exchange: hotel_events
exchange type: topic
```

Producer публикует JSON сообщения с routing key.

## Consumer

Consumer подписывается на события RabbitMQ и обрабатывает их.

У меня consumer:

- подключается к exchange hotel_events
- создает очередь
- подписывается на routing key # (на все события)


Consumer используется для:

- логирования событий
- демонстрации Event-Driven взаимодействия
- асинхронной обработки событий
- CQRS

## В проекте частично применен паттерн CQRS.

Разделение:

1. Commands:
   - create hotel
   - create booking
   - cancele booking
2. Queries:
   - get hotels by city


- Write операции изменяют состояние системы и могут публиковать события.

- Read операции используются для получения данных и дополнительно оптимизированы Redis кешированием.



## Запуск проекта
```
docker compose build
docker compose up
```
## Запуск consumer

Consumer запускается отдельно:
```
docker compose exec api python src/events/consumer.py
```
После запуска он начинает ожидать события

## Проверка работы событий

Пример запроса:

GET /hotels/search?city=Amsterdam

После выполнения запроса:

- API выполняет поиск
- producer публикует event
- consumer получает сообщение

Пример вывода consumer:
```
Событие было получено.....................................
"[{\"id\": \"6a0deff94c2d66fce79df8a3\", \"name\": \"Hilton\", \"city\": \"Amsterdam\", \"address\": \"Center 1\", \"description\": \"Luxury hotel\"}]"
```

#TODO На текущем этапе реализована базовая инфраструктура взаимодействия с RabbitMQ, consumer подключается к очереди, получает сообщения и выводит их в лог. Далее уже можно будет реализовать отправка уведомлений или sms.

### RabbitMQ
RabbitMQ также можно запускаетить с management UI.
```
http://localhost:15672
```
Данные по умолчанию:

login: guest
password: guest

## Event-Driven преимущества

Использование Event-Driven архитектуры позволяет:

- уменьшить связанность компонентов
- выполнять асинхронную обработку
- масштабировать consumers независимо
- реализовать интеграцию между сервисами
- упростить добавление новых обработчиков событий

## Гарантии доставки

В проекте используется модель доставки ```at-least-once delivery```

RabbitMQ гарантирует доставку сообщений подписанным consumers.

# Итог

В рамках задания была реализована полноценная Event-Driven архитектура:

- RabbitMQ broker
- Producer
- Consumer
- Topic exchange
- Routing keys
- Асинхронная обработка событий
- Частичное применение CQRS

Система успешно публикует и обрабатывает события между компонентами приложения.