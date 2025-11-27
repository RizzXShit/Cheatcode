# Write your MySQL query statement below
Select Actor_id, director_id 
from ActorDirector
group by Actor_id, director_id
having count(*) >=3;