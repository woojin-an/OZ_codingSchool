-- (1) customers 테이블에서 특정 고객의 주소를 갱신하세요.
UPDATE customers SET address = '43, Gyeyanggu' WHERE customerID=22;

-- (2) products 테이블에서 특정 제품의 가격을 갱신하세요.
UPDATE products SET price = 1100 WHERE name='water';

-- (3) empLoyees 테이블에서 특정 직원의 직급을 갱신하세요.
UPDATE employees SET position = 'Senior' WHERE name='Gildong';

-- (4) offices 테이블에서 특정 사무실의 전화번호를 갱신하세요.
UPDATE offices SET phone = '032-110-0011' WHERE officeID=22;

-- (5) orders 테이블에서 특정 주문의 상태를 갱신하세요.
UPDATE orders SET status = 'Preparing' WHERE orderID=2;

-- (6) orderdetails 테이블에서 특정 주문 상세의 수량을 갱신하세요.
UPDATE orderdetails SET quantityOrdered = 3 WHERE orderID=2;

-- (7) payments 테이블에서 특정 지불의 금액을 갱신하세요.
UPDATE payments SET amount = 2000 WHERE customerID=2; 

-- (8) productlines 테이블에서 특정 제품 라인의 설명을 갱신하세요.
UPDATE productlines SET textDescription = 'pure water' WHERE name='water';

-- (9) customers 테이블에서 특정 고객의 이메일을 갱신하세요.
UPDATE customers SET email = 'ms@gmail.com' WHERE customerID=1;

-- (10) products 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
UPDATE products SET price = price * 1.20;