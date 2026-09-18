SELECT MAX(salary) AS SecondHighestSalary 
FROM Employee
WHERE salary < (SELECT max(salary) FROM Employee)