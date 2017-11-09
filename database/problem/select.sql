-- select all departments with conditions:
-- 1. All computers in a department have ram>=8
-- 2. A department have only  MAC's
SELECT DEPARTMENT
FROM COMPUTERS
GROUP BY DEPARTMENT
HAVING min(RAM) >= 8 AND
       0 = count(CASE WHEN TYPE = 'PC'
         THEN 1
                        ELSE NULL END)

