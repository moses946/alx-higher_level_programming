-- List all cities contained in the database
SELECT id, name, name
FROM cities
FULL OUTER JOIN states
ON cities.state_id = states.id
