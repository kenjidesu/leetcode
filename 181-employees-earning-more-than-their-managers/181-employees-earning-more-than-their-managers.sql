# Write your MySQL query statement below
SELECT em.name AS Employee
FROM employee em
    INNER JOIN employee emm ON em.managerId = emm.id
WHERE em.salary > emm.salary;