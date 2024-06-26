-- List the number of records with the same score in second_table, sorted by score (descending)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;