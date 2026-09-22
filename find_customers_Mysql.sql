
SELECT Customers
FROM (SELECT c.name AS Customers, o.customerId AS order_id FROM Customers AS c LEFT JOIN Orders AS o ON c.id = o.customerId) AS subg
WHERE order_id IS NULL
