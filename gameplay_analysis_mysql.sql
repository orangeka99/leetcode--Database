WITH MinDate AS (
    SELECT  player_id,event_date,
            CASE WHEN DATEDIFF(event_date, LAG(event_date) OVER(PARTITION BY player_id ORDER BY player_id, event_date)) = 1 THEN 1
                ELSE null
                END AS min_check,
            ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY player_id ASC) AS TTT
    FROM Activity
    ORDER BY player_id, event_date
)
SELECT CASE WHEN r.min_c / l.oo IS NULL THEN 0
            ELSE ROUND((r.min_c / l.oo),2)
            END AS fraction
FROM (
    SELECT player_id,
           COUNT(player_id) OVER() AS oo,
           event_date
    FROM Mindate
    GROUP BY player_id
) l
LEFT JOIN (
    SELECT player_id,
           event_date,COUNT(min_check) OVER() As min_c
    FROM Mindate
    WHERE min_check = 1
    AND TTT = 2
) r
ON l.player_id = r.player_id
ORDER BY min_c DESC
LIMIT 1
