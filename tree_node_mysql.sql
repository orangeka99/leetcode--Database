WITH gg1 AS (
    SELECT 
        l.id AS id_x, 
        l.p_id AS p_id_x,
        r.id AS id_y,
        r.p_id AS p_id_y
    FROM tree as l
    LEFT JOIN tree as r
    ON l.id = r.p_id
)
SELECT id_x AS id,
    CASE WHEN p_id_x IS NULL THEN "Root"
         WHEN id_y IS NULL AND p_id_y IS NULL THEN "Leaf"
         ELSE "Inner"
    END AS type
FROM gg1 
GROUP BY id_x