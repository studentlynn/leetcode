176. Second Highest Salary
# Write your MySQL query statement below
# 是否有第二大的数字（有则 第二大，没有则null）
select 
ifnull(max(Salary),null)
as SecondHighestSalary
from Employee
where Id not in (select Id from Employee
	where Salary in (select max(Salary) from Employee ) 
   )