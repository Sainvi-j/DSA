# Write your MySQL query statement below
select d.name as Department , e.name as Employee, e.salary as Salary
from Employee e
join Department d on e.departmentId =d.id
join(
    select departmentId, max(salary) as max_salary
    from Employee
    group by departmentId
) as dept_max on e.departmentId = dept_max.departmentId and e.salary = dept_max.max_salary;