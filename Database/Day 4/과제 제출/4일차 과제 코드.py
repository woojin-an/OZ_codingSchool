import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='oz-password',
    db='airbnb',
)

try:
    with conn.cursor() as cursor:
        # 문제 1 새제품 추가
        sql = "INSERT INTO Products (productName, price) VALUES (%s, %s)"
        cursor.execute(sql, ('Python Book', 29.99))
        conn.commit()
    
        # 문제 2: 고객 목록 조회
        sql = "SELECT * FROM Customers"
        cursor.execute(sql)
        
        # 문제 3: 제품 재고 업데이트
        sql = "UPDATE Products SET stockQuantity = stockQuantity - 1 WHERE productID = %s"
        cursor.execute(sql, (stockQuantity, productID))
        conn.commit()
        # 4. 고객별 총 주문 금액 계산: 'Orders' 테이블을 사용하여 각 고객별로 총 주문 금액을 계산하는 Python 스크립트를 작성하세요.
        sql = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"
        cursor.execute(sql)

        # 5. 고객 이메일 업데이트: 고객의 이메일 주소를 업데이트하는 Python 스크립트를 작성하세요. 고객 ID를 입력받고, 새로운 이메일 주소로 업데이트합니다.
        sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
        cursor.execute(sql, (newEmail, customerID))
        conn.commit()
        
        # 6. 주문 취소: 주문을 취소하는 Python 스크립트를 작성하세요. 주문 ID를 입력받아 해당 주문을 'Orders' 테이블에서 삭제합니다.
        sql = "DELETE FROM Orders WHERE orderID = %s"
        cursor.execute(sql, (orderID))
        conn.commit()
        
        # 7. 특정 제품 검색: 제품 이름을 기반으로 'Products' 테이블에서 제품을 검색하는 Python 스크립트를 작성하세요.
        sql = "SELECT * FROM Products WHERE productName LIKE %s"
        cursor.execute(sql, ('%Book%'))

        # 8. 특정 고객의 모든 주문 조회: 고객 ID를 기반으로 그 고객의 모든 주문을 조회하는 Python 스크립트를 작성하세요.
        sql = "SELECT * FROM Orders WHERE customerID = %s"
        cursor.execute(sql, (customerID))
               
        # 9. 가장 많이 주문한 고객 찾기: 'Orders' 테이블을 사용하여 가장 많은 주문을 한 고객을 찾는 Python 스크립트를 작성하세요.
        sql = "SELECT customerID, COUNT(*) AS orderCount FROM Orders GROUP BY customerID ORDER BY orderCount DESC LIMIT 1"
        cursor.execute(sql)

finally:
    conn.close()