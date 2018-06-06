177. Nth Highest Salary
# 主要要注意函数的用法
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET @int_i = 0;
  RETURN (
      # Write your MySQL query statement below.
      # 排名为n的薪水

	  select  Salary_d
	  from ( 
      SELECT @int_i:=@int_i+1 as id, Salary_d
      from (select distinct Salary as Salary_d from Employee) e
	  order by Salary_d desc
	  ) e_d
	  where id = N

  );
END

"""
CREATE TABLE Employee (
  Id INT PRIMARY KEY,
  Salary INT
) ENGINE=INNODB;


INSERT INTO Employee VALUES 
(1,100),
(2,200),
(3,300);
INSERT INTO test VALUES (200,200,\'200test_nagios\');
"""