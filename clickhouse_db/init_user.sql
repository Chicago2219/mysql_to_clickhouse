-- Создаём пользователя, если ещё не создан
CREATE USER IF NOT EXISTS custom_user IDENTIFIED WITH plaintext_password BY '0000';

-- Даём все права на все базы и таблицы
GRANT CREATE, ALTER, DROP, INSERT, SELECT, UPDATE, TRUNCATE, DELETE ON *.* TO custom_user;

