-- select dat from 2 tables
SELECT cities.id, cities.name, states.name
FROM cities c NATURAL JOIN states s
ORDER BY c.id;
