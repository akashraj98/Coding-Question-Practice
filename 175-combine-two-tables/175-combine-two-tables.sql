# Write your MySQL query statement below
SELECT P.firstName, P.lastName, A.city, A.state
FROM PERSON P
LEFT JOIN ADDRESS A
ON P.PERSONID = A.PERSONID;