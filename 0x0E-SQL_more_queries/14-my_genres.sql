-- List all genres of show Dexter
SELECT DISTINCT name
FROM tv_genres
JOIN tv_show_genres t
ON t.genre_id = genre_id
JOIN tv_shows s
ON s.id = t.show_id
WHERE s.title = 'Dexter'
ORDER BY name ;
