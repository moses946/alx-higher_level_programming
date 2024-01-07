-- List shows without any genre linked
SELECT title, IFNULL(t.genre_id, 'NULL') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres t
ON id = t.show_id
WHERE genre_id IS  NULL
ORDER BY title ASC, t.genre_id ASC;
