-- Display Max temp of each state
SELECT state, MAX(`value`) FROM value GROUP BY state ORDER BY state;
