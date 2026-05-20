workspace "Hotel Booking System" "Система бронирования отелей" {

    model {

        user = person "Пользователь" "Ищет отели и создает бронирования"

        admin = person "Администратор" "Управляет информацией об отелях"

        paymentSystem = softwareSystem "Payment System" "Внешняя платежная система"

        emailSystem = softwareSystem "Email Service" "Сервис отправки email уведомлений"

        bookingSystem = softwareSystem "Hotel Booking System" "Система бронирования отелей" {

            webApp = container "Web Application" "Пользовательский веб-интерфейс системы бронирования" "React"

            apiGateway = container "API Gateway" "Единая точка входа для клиентских запросов" "REST API"

            userService = container "User Service" "Управление пользователями" "Spring Boot REST API"

            hotelService = container "Hotel Service" "Управление отелями и поиском" "Spring Boot REST API"

            bookingService = container "Booking Service" "Создание и отмена бронирований" "Spring Boot REST API"

            notificationService = container "Notification Service" "Отправка уведомлений пользователям" "Spring Boot"

            database = container "PostgreSQL Database" "Хранение данных системы" "PostgreSQL"

            user -> webApp "Использует систему"

            admin -> webApp "Управляет отелями"

            webApp -> apiGateway "HTTPS"

            apiGateway -> userService "REST API"
            apiGateway -> hotelService "REST API"
            apiGateway -> bookingService "REST API"

            userService -> database "Чтение/запись пользователей" "JDBC"

            hotelService -> database "Чтение/запись отелей" "JDBC"

            bookingService -> database "Чтение/запись бронирований" "JDBC"

            bookingService -> hotelService "Проверка доступности отеля" "REST API"

            bookingService -> paymentSystem "Оплата бронирования" "HTTPS/REST"

            notificationService -> emailSystem "Отправка email уведомлений" "SMTP/API"
        }

        user -> bookingSystem "Ищет отели и создает бронирования"

        admin -> bookingSystem "Управляет отелями"

        bookingSystem -> paymentSystem "Выполняет оплату бронирований"

        bookingSystem -> emailSystem "Отправляет уведомления"
    }

    views {

        systemContext bookingSystem {

            include *

            autolayout lr

            title "System Context Diagram - Hotel Booking System"
        }

        container bookingSystem {

            include *

            autolayout lr

            title "Container Diagram - Hotel Booking System"
        }

        dynamic bookingSystem "Создание бронирования" {

            user -> webApp "Выбирает отель и создает бронирование"

            webApp -> apiGateway "POST /bookings"

            apiGateway -> bookingService "Создать бронирование"

            bookingService -> userService "Проверка пользователя"

            userService -> bookingService "Пользователь найден"

            bookingService -> hotelService "Проверка доступности отеля"

            hotelService -> bookingService "Отель доступен"

            bookingService -> database "Сохранение бронирования"

            bookingService -> paymentSystem "Оплата бронирования"

            paymentSystem -> bookingService "Оплата успешна"

            notificationService -> emailSystem "Отправка email"

            bookingService -> apiGateway "Бронирование создано"

            apiGateway -> webApp "HTTP 201 Created"

            autolayout lr
        }

        theme default
    }
}