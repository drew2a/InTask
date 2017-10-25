-- select all departments with conditions:
-- 1. all computers have ram>=8
-- 2. department have only  MAC's
SELECT DEPARTMENT
FROM COMPUTERS
GROUP BY DEPARTMENT
HAVING min(RAM) >= 8 AND
       0 = count(CASE WHEN TYPE = 'PC'
         THEN 1
                        ELSE NULL END)

