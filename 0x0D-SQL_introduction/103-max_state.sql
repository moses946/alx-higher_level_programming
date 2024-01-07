-- Display Max temp of each state
SELECT state, MAX(`value`) FROM temp GROUP BY state ORDER BY state;
