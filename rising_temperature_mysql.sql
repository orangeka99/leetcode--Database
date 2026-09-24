SELECT subq.id
FROM (SELECT id,
        CASE 
            WHEN LAG(temperature) OVER (ORDER BY recordDate ASC) < temperature 
                AND DATE_ADD(LAG(recordDate) OVER (ORDER BY recordDate ASC), INTERVAL 1 DAY) = recordDate 
            THEN 1
            ELSE 0
        END AS gg
       FROM Weather) AS subq
WHERE gg = 1