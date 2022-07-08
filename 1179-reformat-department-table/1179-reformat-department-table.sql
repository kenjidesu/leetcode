# Write your MySQL query statement below
SELECT DISTINCT D.id, 
    (SELECT revenue FROM department WHERE month = 'Jan' AND D.id = id) AS 'Jan_Revenue',
    (SELECT revenue FROM department WHERE month = 'Feb' AND D.id = id) AS 'Feb_Revenue',
    (SELECT revenue FROM department WHERE month = 'Mar' AND D.id = id) AS 'Mar_Revenue',
    (SELECT revenue FROM department WHERE month = 'Apr' AND D.id = id) AS 'Apr_Revenue',
    (SELECT revenue FROM department WHERE month = 'May' AND D.id = id) AS 'May_Revenue',
    (SELECT revenue FROM department WHERE month = 'Jun' AND D.id = id) AS 'Jun_Revenue',
    (SELECT revenue FROM department WHERE month = 'Jul' AND D.id = id) AS 'Jul_Revenue',
    (SELECT revenue FROM department WHERE month = 'Aug' AND D.id = id) AS 'Aug_Revenue',
    (SELECT revenue FROM department WHERE month = 'Sep' AND D.id = id) AS 'Sep_Revenue',
    (SELECT revenue FROM department WHERE month = 'Oct' AND D.id = id) AS 'Oct_Revenue',
    (SELECT revenue FROM department WHERE month = 'Nov' AND D.id = id) AS 'Nov_Revenue',
    (SELECT revenue FROM department WHERE month = 'Dec' AND D.id = id) AS 'Dec_Revenue'
FROM (
    SELECT DISTINCT id
    FROM department
) AS D

