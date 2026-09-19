WITH GroupedData AS ( 
SELECT
    id,
    num,
    COUNT(*) OVER (PARTITION BY num, group_id) AS group_count
FROM (SELECT
        id,
        num ,
        CAST(ROW_NUMBER() OVER (ORDER BY id) AS SIGNED) 
        - CAST(ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS SIGNED) AS group_id
    FROM Logs ) AS Sub
ORDER BY id ASC
)
SELECT num AS ConsecutiveNums 
FROM GroupedData
WHERE group_count > 2
GROUP BY num






