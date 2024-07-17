USE testdatabase;

-- 초급 생성 (CREATE) 
-- 1. customers 테이블에 새 고객 추가
INSERT INTO customers (name, address) VALUES ('Minsu', '224, Jongro-gu');

-- 2. products 테이블에 새 제품 추가
INSERT INTO products (name, price) VALUES ('water', 1000);

-- 3. employees 테이블에 새 직원 추가
INSERT INTO employees (name, position) VALUES ('Gildong', 'Junior');

-- 4. offices 테이블에 새 사무실 추가
INSERT INTO offices (location, phone) VALUES ('SEOUL', '02-110-0011');

-- • (5) orders 테이블에 새 주문을 추가하세요.
INSERT INTO orders (orderDate, customerID) VALUES ('2024-07-17', 1);

-- • (6) orderdetails 테이블에 주문 상세 정보를 추가하세요.
INSERT INTO orderdetails (productID, quantityOrdered) VALUES (1, 2);

-- • (7) payments 테이블에 지불 정보를 추가하세요.
INSERT INTO payments (customerID, amount) VALUES (1, 2000);

-- • (8) productlines 테이블에 제품 라인을 추가하세요.
INSERT INTO productlines (productLine, textDescription) VALUES ('Drink', 'Something to drink');

-- • (9) customers 테이블에 다른 지역의 고객을 추가하세요.
INSERT INTO customers (name, address, city) VALUES ('Minji', '3, Bupyeong-gu', 'Incheon');

-- • (10) products 테이블에 다른 카테고리의 제품을 추가하세요.
INSERT INTO products (name, price, productLine) VALUES ('Chips', 1200, 'Snack');