-- List all shows in the database
SELECT title, IFNULL(genre_id, 'NULL') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres t
ON id = t.show_id
ORDER BY title ASC, t.genre_id ASC;
