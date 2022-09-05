# Write your MySQL query statement below
# SELECT 
# IFNULL((SELECT distinct salary  
# FROM Employee 
# order by Salary 
# desc limit 1 offset 1),NULL) AS SecondHighestSalary

SELECT MAX(SALARY) AS SecondHighestSalary
from Employee
where salary < (select max(salary) from Employee)