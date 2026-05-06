SELECT title, AVG(salary_max) AS avg_salary
FROM jobs
GROUP BY title
ORDER BY avg_salary DESC;