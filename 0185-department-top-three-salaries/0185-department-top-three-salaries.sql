# Write your MySQL query statement below
select d.name as Department, ranked.name as Employee, ranked.salary as Salary
from(
    select e.name, e.salary, e.departmentId ,
    dense_rank() over (partition by e.departmentId order by e.salary desc) as salary_rank
    from Employee e
) as ranked
join Department d on ranked.departmentId = d.id
where ranked.salary_rank <= 3;