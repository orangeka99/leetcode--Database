SELECT d.name AS Department, subq.Employee, subq.Salary
FROM (SELECT name AS Employee, salary AS Salary, departmentId, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS gg FROM Employee) AS subq
INNER JOIN Department AS d
ON subq.departmentId = d.id
WHERE subq.gg <= 3
