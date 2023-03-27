INSERT INTO customers (name, tg_id) VALUES 
('Test Test', 123456),
('Test Value', 012345),
('Hello Tester', 555555)
ON CONFLICT (tg_id) DO NOTHING;

INSERT INTO orders (id, description, from_address, to_address, units, weight, phone, tg_id) VALUES
('1', 'Test description', 'Moscow', 'London', 'Kg', 10, +77777777777, 123456),
('2', 'Hello Tester! This is description', 'New York', 'LA', 'Kg', 10, +77777777777, 123456),
('3', 'Test description number 2!', 'Oral', 'Astana', 'Kg', 10, +77777777777, 123456)
ON CONFLICT (id) DO NOTHING;