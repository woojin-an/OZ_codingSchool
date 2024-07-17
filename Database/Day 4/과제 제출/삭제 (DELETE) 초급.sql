-- (1) customers 테이블에서 특정 고객을 삭제하세요.
DELETE FROM custmoers WHERE customerID=1;

-- (2) products 테이블에서 특정 제품을 삭제하세요.
DELETE FROM products WHERE productID=1;

-- (3) employees 테이블에서 특정 직원을 삭제하세요.
DELETE FROM employees WHERE employeeID=1;

-- (4) offices 테이블에서 특정 사무실을 삭제하세요.
DELETE FROM offices WHERE officeID=1;

-- (5) orders 테이블에서 특정 주문을 삭제하세요.
DELETE FROM orders WHERE orderID=1;

-- (6) orderdetails 테이블에서 특정 주문 상세를 삭제하세요.
DELETE FROM orderdetails WHERE orderID=1;

-- (7) payments 테이블에서 특정 지불 내역을 삭제하세요.
DELETE FROM payments WHERE customerID=1;

-- (8) productlines 테이블에서 특정 제품 라인을 삭제하세요.
DELETE FROM productlines WHERE productLine='drink'; 

-- (9) customers 테이블에서 특정 지역의 모든 고객을 삭제하세요.
DELETE FROM customers WHERE city='SEOUL';

-- (10) products 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
DELETE FROM products WHERE productLine='Snack';