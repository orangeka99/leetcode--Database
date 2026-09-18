CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
DECLARE
    offset_val INT := CASE
                        WHEN N - 1 < 0 THEN 100
                        ELSE N - 1
                      END;
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT E.salary
    FROM Employee AS E
    GROUP BY E.salary
    ORDER BY E.salary DESC
    LIMIT 1 OFFSET offset_val
      
  );
END;
$$ LANGUAGE plpgsql;