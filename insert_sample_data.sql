-- Insert Customers
INSERT INTO customers (id, name, email, phone) VALUES
(1, 'John Doe', 'jd1@email.com', '555-1234'),
(2, 'Jane Smith', 'js2@email.com', '555-5678'),
(3, 'Mike Allen', 'ma3@email.com', '555-9999'),
(4, 'Lisa Ray', 'lr4@email.com', '555-4321'),
(5, 'Tom Fox', 'tf5@email.com', '555-9876');

-- Insert Salespeople
INSERT INTO salespeople (id, name, email) VALUES
(1, 'Carl', 'carl@email.com'),
(2, 'Dave', 'dave@email.com'),
(3, 'Eve', 'eve@email.com'),
(4, 'Rob', 'rob@email.com'),
(5, 'Nina', 'nina@email.com');

-- Insert Cars
INSERT INTO cars (id, vin, make, model, year, customer_id, salesperson_id) VALUES
(1, 'VIN001', 'Toyota', 'Camry', 2021, 1, 1),
(2, 'VIN002', 'Ford', 'F-150', 2019, 2, 2),
(3, 'VIN003', 'Tesla', 'Model 3', 2020, 3, 3),
(4, 'VIN004', 'Honda', 'Civic', 2022, 4, 4),
(5, 'VIN005', 'Chevy', 'Malibu', 2018, 5, 5);

-- Insert Invoices
INSERT INTO invoices (id, amount, date, car_id, salesperson_id, customer_id) VALUES
(1, 100, '2023-01-01', 1, 1, 1),
(2, 200, '2023-02-15', 2, 2, 2),
(3, 300, '2023-03-20', 3, 3, 3),
(4, 400, '2023-04-05', 4, 4, 4),
(5, 500, '2023-05-10', 5, 5, 5);

-- Insert Mechanics
INSERT INTO mechanics (id, name, specialty) VALUES
(1, 'Mac', 'Engines'),
(2, 'Jess', 'Brakes'),
(3, 'Vic', 'Electrical'),
(4, 'Sky', 'Suspension'),
(5, 'Terry', 'General');

-- Insert Service Tickets
INSERT INTO service_tickets (id, car_id, customer_id, description, date) VALUES
(1, 1, 1, 'Oil change', '2023-06-01'),
(2, 2, 2, 'Brake inspection', '2023-06-05'),
(3, 3, 3, 'Battery replacement', '2023-06-10'),
(4, 4, 4, 'Tire rotation', '2023-06-15'),
(5, 5, 5, 'Check engine light', '2023-06-20');

-- Insert Mechanic-Car Links
INSERT INTO mechanic_car_link (id, mechanic_id, car_id) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5);
