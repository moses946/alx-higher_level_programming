-- List all comedy shows
SELECT title
FROM tv_shows
JOIN tv_show_genres t
ON t.show_id = id
JOIN tv_genres g
ON t.genre_id = g.id
WHERE g.name = "Comedy"
ORDER BY title ASC;
