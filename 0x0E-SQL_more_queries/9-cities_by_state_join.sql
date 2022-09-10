-- select dat from 2 tables
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=sates.id
ORDER BY cities.id;
