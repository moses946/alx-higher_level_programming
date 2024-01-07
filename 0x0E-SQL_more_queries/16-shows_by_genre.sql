-- List all shows and genres linked to it
SELECT title, IFNULL(g.name, "NULL") AS name
FROM tv_shows
LEFT JOIN tv_show_genres t
ON id = t.show_id
LEFT JOIN tv_genres g
ON g.id = t.genre_id
ORDER BY title ASC, name ASC;
