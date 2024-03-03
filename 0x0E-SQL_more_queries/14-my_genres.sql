-- List all genres of show Dexter
SELECT DISTINCT g.name
FROM tv_genres g
JOIN tv_show_genres t
ON t.genre_id = g.genre_id
JOIN tv_shows s
ON s.id = t.show_id
WHERE s.title = 'Dexter'
ORDER BY g.name ;
