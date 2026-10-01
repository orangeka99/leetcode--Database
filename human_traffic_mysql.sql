WITH l1 AS (
    SELECT 
            id,
            visit_date,
            people,
            LEAD(people,1) OVER() AS next_1,
            LEAD(people,2) OVER() AS next_2,
            LAG(people,1) OVER() AS prev_1,
            LAG(people,2) OVER() AS prev_2
    FROM Stadium
),
l2 AS (
    SELECT  id,
            visit_date,
            people,
            CASE WHEN people >= 100 AND next_1 >= 100 AND next_2 >= 100 THEN True
                WHEN people >= 100 AND prev_1 >= 100 AND prev_2 >= 100 THEN True
                WHEN people >= 100 AND prev_1 >= 100 AND next_1 >= 100 THEN True
                ELSE False 
            END AS chk
    FROM l1
)
SELECT id,visit_date,people
FROM l2
WHERE chk = 1

