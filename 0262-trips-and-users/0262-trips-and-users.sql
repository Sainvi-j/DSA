# Write your MySQL query statement below
select
Request_at as Day,
round(sum(Status in ('cancelled_by_driver', 'cancelled_by_client'))/count(*),2) as 'Cancellation Rate'
from Trips
where
Client_Id not in (select Users_Id from Users where Banned ='Yes' and Role = 'client') and
Driver_Id not in (select Users_Id from Users where Banned ='Yes' and Role = 'driver') and
Request_at between '2013-10-01' and '2013-10-03'
group by Request_at;