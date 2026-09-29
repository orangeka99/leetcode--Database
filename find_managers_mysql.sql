
SELECT  e.name
FROM Employee AS e
INNER JOIN (SELECT id,managerId,COUNT(*) OVER(PARTITION BY managerId) AS gg
    FROM Employee) AS c
ON e.id = c.managerId
AND c.gg > 4
GROUP BY e.id,e.name
