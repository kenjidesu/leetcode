# Write your MySQL query statement below
SELECT e.employee_id
FROM Employees e
WHERE e.employee_id NOT IN
    (SELECT e.employee_id
     FROM Employees e
        INNER JOIN Salaries s ON e.employee_id = s.employee_id)
UNION
SELECT s.employee_id
FROM Salaries s
WHERE s.employee_id NOT IN
    (SELECT s.employee_id
     FROM Salaries s
        INNER JOIN Employees e ON s.employee_id = e.employee_id)
ORDER BY employee_id ASC;