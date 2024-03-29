SELECT MP.MEMBER_NAME, RR.REVIEW_TEXT, DATE_FORMAT(RR.REVIEW_DATE,'%Y-%m-%d')
FROM REST_REVIEW RR
JOIN MEMBER_PROFILE MP
ON RR.MEMBER_ID=MP.MEMBER_ID
WHERE MP.MEMBER_ID IN 
(SELECT MP.MEMBER_ID
FROM REST_REVIEW RR
JOIN MEMBER_PROFILE MP
ON RR.MEMBER_ID=MP.MEMBER_ID
GROUP BY RR.MEMBER_ID
HAVING COUNT(*)=
    (SELECT MAX(A.CNT)
    FROM (SELECT COUNT(*) AS CNT
        FROM REST_REVIEW
        GROUP BY MEMBER_ID) A))
ORDER BY REVIEW_DATE ASC, REVIEW_TEXT ASC