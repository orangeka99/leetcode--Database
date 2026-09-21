SELECT l.name AS Employee 
FROM Employee AS l
JOIN Employee AS r
ON l.managerId = r.id
AND l.salary  > r.salary
