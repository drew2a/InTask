SELECT
  d.dept_id,
  e.c,
  sum_of_salary
FROM (
       SELECT
         dept_id,
         count(*)             AS c,
         sum(EMPLOYEE.SALARY) AS sum_of_salary
       FROM EMPLOYEE
       GROUP BY dept_id
       ORDER BY DEPT_ID) AS e
  JOIN DEPARTMENT AS d
    ON e.DEPT_ID = d.dept_id
WHERE e.c > 0



