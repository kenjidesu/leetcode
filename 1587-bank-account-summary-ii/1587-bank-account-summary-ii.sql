# Write your MySQL query statement below
SELECT u.name, SUM(t.amount) AS balance
FROM users u
    INNER JOIN transactions t ON u.account = t.account
GROUP BY t.account
HAVING balance > 10000;
