-- 1번
CREATE TABLE employees(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10,2)
);
USE testdatabase;

-- 2번
INSERT INTO employees (name, position, salary) VALUES ('혜린', 'PM', 90000);
INSERT INTO employees (name, position, salary) VALUES ('은우', 'Frontend', 80000);
INSERT INTO employees (name, position, salary) VALUES ('가을', 'Backend', 92000);
INSERT INTO employees (name, position, salary) VALUES ('지수', 'Frontend', 78000);
INSERT INTO employees (name, position, salary) VALUES ('민혁', 'Frontend', 96000);
INSERT INTO employees (name, position, salary) VALUES ('하온', 'Backend', 130000);

-- 3번
SELECT name, salary FROM employees;

-- 4번
SELECT name, salary FROM employees WHERE position = 'Frontend' AND salary <= 90000;

-- 5번
UPDATE employees SET salary = salary * 1.10 WHERE position = 'PM';
SELECT * FROM employees WHERE position = 'PM';

-- 6번
UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend';

-- 7번
DELETE FROM employees WHERE name = '민혁';

-- 8번
SELECT position, AVG(salary) AS average_salary FROM employees GROUP BY position;

-- 9번
-- DROP TABLE employees;