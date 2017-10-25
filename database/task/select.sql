-- select all departments with conditions:
-- 1. all computers have ram>=8
-- 2. department have only  MAC's
select DEPARTMENT
FROM COMPUTERS
GROUP by DEPARTMENT
HAVING min(RAM)>=8 AND
count(*)=count(case when TYPE = 'MAC' then 1 else null end)

