CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  declare M int;
  set M = N - 1;
  RETURN (
      select distinct salary
      from Employee
      order by salary desc
      limit 1 OFFSET M
  );
END