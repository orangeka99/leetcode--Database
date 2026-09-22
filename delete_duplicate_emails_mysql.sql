DELETE l FROM Person AS l
INNER JOIN Person AS r
ON l.email = r.email
AND l.id > r.id