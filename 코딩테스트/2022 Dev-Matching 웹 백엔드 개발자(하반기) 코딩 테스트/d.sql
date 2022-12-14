SELECT
P.ID, P.NAME, T.COUNT AS '임대 가능일'
FROM
PLACES P,(SELECT
ID, COUNT(*) AS COUNT 
FROM
PLACES, SCHEDULES
WHERE
ID=PLACE_ID
GROUP BY
ID
HAVING
COUNT(*)>0) AS T
WHERE
P.ID=T.ID