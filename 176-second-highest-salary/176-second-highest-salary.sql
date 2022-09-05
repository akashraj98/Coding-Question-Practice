# Write your MySQL query statement below
SELECT 
(SELECT distinct salary  
FROM Employee 
order by Salary 
desc limit 1 offset 1) AS SecondHighestSalary