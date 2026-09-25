SELECT player_id, first_login
FROM (SELECT player_id, event_date AS first_login,ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY player_id, event_date ASC) AS hh
FROM Activity 
) AS subq
WHERE hh = 1

