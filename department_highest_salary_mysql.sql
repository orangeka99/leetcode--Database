SELECT r.name AS Department, dept.Employee, dept.Salary
FROM (SELECT name AS Employee, salary AS Salary,departmentId, MAX(salary) OVER (PARTITION BY departmentId) AS gg FROM Employee) AS dept
INNER JOIN Department AS r
ON dept.departmentId = r.id
WHERE Salary = gg


