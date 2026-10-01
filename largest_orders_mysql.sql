WITH l1 AS (
    SELECT order_number,customer_number,COUNT(*) OVER(PARTITION BY customer_number) AS GG
    FROM Orders

) 
SELECT customer_number
FROM l1
ORDER BY GG DESC
LIMIT 1