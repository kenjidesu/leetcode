# Write your MySQL query statement below
SELECT DISTINCT email
FROM person
GROUP BY email
HAVING COUNT(email) > 1