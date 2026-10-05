WITH gg1 AS (
    SELECT requester_id
    FROM RequestAccepted 
    UNION ALL
    SELECT accepter_id
    FROM RequestAccepted
)
SELECT requester_id AS id, COUNT(*) OVER(PARTITION BY requester_id) AS num
FROM gg1
ORDER BY num DESC LIMIT 1
