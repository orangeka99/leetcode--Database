WITH Top3Emp AS(
    SELECT 
        departmentId,
        name AS Employee,
        salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS gg
    FROM Employee
)
SELECT d.name AS Department,e.Employee,e.Salary
FROM Top3Emp As e
INNER JOIN Department AS d
ON e.departmentId = d.id
WHERE e.gg <= 3