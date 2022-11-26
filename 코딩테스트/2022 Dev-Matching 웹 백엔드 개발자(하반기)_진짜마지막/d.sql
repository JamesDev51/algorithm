SELECT 
b.id AS BRANCH_ID, b.name AS BRANCH_NAME, COUNT(s.car_id) AS COUNT
FROM 
BRANCHES b LEFT OUTER JOIN EMPLOYEES e ON b.id=e.branch_id 
LEFT OUTER JOIN (
    SELECT * FROM SELLINGS 
    WHERE car_id=306
) s ON e.id=s.employee_id
GROUP BY
b.id,b.name
ORDER BY
b.id
