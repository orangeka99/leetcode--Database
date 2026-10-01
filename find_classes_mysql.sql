WITH l1 AS (
    SELECT class,COUNT(*) OVER(PARTITION BY class) AS gg
    FROM Courses
)
SELECT class
FROM l1
WHERE gg > 4
GROUP BY class




