INSERT INTO users(login, password, first_name, last_name)
VALUES
('admin', '123', 'John', 'Doe'),
('user1', '123', 'Alice', 'Smith');

INSERT INTO hotels(name, city, address, description)
VALUES
('Hilton', 'Amsterdam', 'Center', 'Luxury hotel'),
('Marriott', 'Paris', 'Street 1', 'Business hotel');

INSERT INTO bookings(user_id, hotel_id, check_in, check_out)
VALUES
(1, 1, '2026-06-01', '2026-06-10'),
(2, 2, '2026-07-01', '2026-07-05');