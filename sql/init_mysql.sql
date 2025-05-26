
CREATE TABLE orders (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  amount DECIMAL(10,2),
  created_at DATETIME
);

INSERT INTO orders (user_id, amount, created_at)
VALUES (1, 2500.50, NOW()), (2, 990.00, NOW());
