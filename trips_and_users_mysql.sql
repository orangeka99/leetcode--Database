WITH JoinData AS(
    SELECT  
            t1.status,
            t1.request_at,
            ROUND((COUNT(*) OVER (PARTITION BY t1.request_at, t1.status) / COUNT(*) OVER (PARTITION BY t1.request_at)), 2) AS yy,
            ROW_NUMBER() OVER (PARTITION BY t1.request_at ORDER BY t1.id DESC) AS jjj,
            COUNT(*) OVER() AS GGGG
    FROM Trips AS t1
    INNER JOIN Users AS t2 ON t1.client_id = t2.users_id AND t2.banned = 'No'
    INNER JOIN Users AS t3 ON t1.driver_id = t3.users_id AND t3.banned = 'No'
    WHERE t1.request_at BETWEEN '2013-10-01' AND '2013-10-03'

)
SELECT request_at AS 'Day',CASE 
                              WHEN yy = 1 AND GGGG = 1 AND status <> 'completed' THEN 1
                              WHEN yy = 1 AND GGGG = 1 AND status = 'completed' THEN 0
                              WHEN yy = 1 THEN ROUND(0,2)
                              ELSE yy
                              END AS "Cancellation Rate"  FROM JoinData WHERE jjj = 1







