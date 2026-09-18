CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE offset_val INT;
--   DECLARE min_val INT;
--   DECLARE max_val INT;
  DECLARE count_val INT;
  SET offset_val = N - 1;
--   SELECT MIN(salary), MAX(salary), COUNT(salary) INTO min_val, max_val, count_val FROM Employee;
--   IF min_val = max_val AND count_val = N AND N != 1 THEN
--         RETURN NULL;
--   END IF;
  RETURN (
      # Write your MySQL query statement below.
    SELECT salary
    FROM Employee
    GROUP BY salary
    ORDER BY salary DESC
    LIMIT 1 OFFSET offset_val
    

  );
END