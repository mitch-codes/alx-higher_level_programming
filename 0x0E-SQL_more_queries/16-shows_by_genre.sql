-- select dat from 2 tables
SELECT tv_shows.title, tv_genres.name
FROM tv_shows JOIN tv_show_genres
JOIN tv_genres
ORDER BY tv_shows.title, tv_genres.name;
