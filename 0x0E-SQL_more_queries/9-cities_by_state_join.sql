-- select dat from 2 tables
SELECT cities.id, cities.name, states.name
FROM cities c LEFT JOIN states s
ON c.state_id = s.id
ORDER BY c.id;
