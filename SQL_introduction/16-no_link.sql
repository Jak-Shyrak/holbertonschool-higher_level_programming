
-- List all records from second_table excluding rows without a name value, displaying score and name, ordered by score (descending)
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;