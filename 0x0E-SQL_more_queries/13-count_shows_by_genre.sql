-- select dat from 2 tables
SELECT tv_genres.name AS genre, count(tv_genres.name) AS number_of_shows
FROM tv_shows join tv_show_genres
ON tv_shows.id=tv_show_genres.show_id join tv_genres 
ON tv_show_genres.genre_id=tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
