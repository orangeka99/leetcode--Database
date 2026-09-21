SELECT email AS Email
FROM (SELECT DISTINCT email, COUNT(*) OVER (PARTITION BY email) AS count_mail FROM Person) AS sub_g
WHERE count_mail > 1
