USE yes24;
-- 기본 조회 및 필터링
-- SELECT title, author FROM books;
-- SELECT * FROM books WHERE rating >= 4.0;
-- SELECT title, review FROM books WHERE review >= 100 ORDER BY review DESC;
-- SELECT title, price FROM books WHERE price <= 20000;
-- SELECT * FROM books WHERE ranking_weeks >= 4 ORDER BY ranking_weeks DESC;
-- SELECT * FROM books WHERE author = '최태성 저';
-- SELECT * FROM books WHERE publisher = '이투스북';

-- 조인 및 관계
SELECT author, COUNT(*) FROM books GROUP BY author ORDER BY count(*) DESC;
SELECT publisher, COUNT(*) AS publishing_count FROM books GROUP BY publisher ORDER BY publishing_count DESC LIMIT 5;
SELECT author, AVG(rating) AS rating_avg FROM books GROUP BY author ORDER BY rating_avg DESC LIMIT 10;
SELECT * FROM books WHERE ranking = 1;
SELECT title, sales, review FROM books ORDER BY sales DESC, review DESC LIMIT 10;
SELECT * FROM books ORDER BY publishing DESC LIMIT 5;

-- 집계 및 그룹화
SELECT author, AVG(rating) FROM books GROUP BY author;
SELECT publishing, COUNT(*) FROM books GROUP BY publishing ORDER BY publishing DESC;
SELECT title, AVG(price) AS price_avg FROM books GROUP BY title ORDER BY price_avg DESC;
SELECT * FROM books ORDER BY review DESC LIMIT 5;
SELECT ranking, AVG(review) FROM books GROUP BY ranking ORDER BY ranking DESC;

-- 서브쿼리 및 고급 기능
-- SELECT title, rating FROM books WHERE rating > (SELECT AVG(rating) FROM books) ORDER BY rating ASC;
-- SELECT title, price FROM books WHERE price > (SELECT AVG(price) FROM books)
-- SELECT title, review FROM books WHERE review > (SELECT MAX(review) FROM books);
-- SELECT title, sales FROM books WHERE sales < (SELECT AVG(sales) FROM books) ORDER BY sales DESC;
SELECT title, author FROM books WHERE author = (
SELECT author FROM books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1
);

-- 데이터 수정 및 관리
-- UPDATE books SET price = 9999 WHERE title = '최소한의 한국사';
-- UPDATE books SET title = '최대한의 한국사' WHERE title = '최소한의 한국사';
-- DELETE FROM books WHERE sales = (SELECT MIN(sales) FROM books);
-- UPDATE books SET rating = rating+1 WHERE publisher = '이투스북';

-- 데이터 분석 예제
SELECT author, AVG(rating), AVG(sales) FROM books GROUP BY author ORDER BY AVG(rating) DESC;
SELECT publishing, AVG(price) FROM books GROUP BY publishing ORDER BY publishing ASC;
SELECT publisher, COUNT(*) AS book_count, SUM(review) AS review_sum FROM books GROUP BY publisher ORDER BY book_count DESC;
SELECT ranking, AVG(sales) FROM books GROUP BY ranking;
SELECT price, AVG(review), AVG(rating) FROM books GROUP BY price ORDER BY price ASC;

-- 난이도 있는 문제
SELECT publisher, author, AVG(sales) as avg_sales
FROM books
GROUP BY publisher, author
ORDER BY publisher, avg_sales DESC;

SELECT title, review, price 
FROM books 
WHERE review > (SELECT AVG(review) FROM books) 
AND price < (SELECT AVG(price) FROM books);

SELECT author, COUNT(distinct title) as num_books
from books
group by author
order by num_books desc
limit 1;

SELECT author, max(sales) from books
group by author;

SELECT YEAR(publishing) as year, COUNT(*) as num_books, avg(price) as avg_price
from books
group by year
order by year desc;

SELECT publisher, max(rating) - min(rating) as rating_dif
from books
group by publisher
order by rating_dif desc;

SELECT title, rating / sales as ratio
from books
where author = '최태성 저'
order by ratio desc
limit 1;