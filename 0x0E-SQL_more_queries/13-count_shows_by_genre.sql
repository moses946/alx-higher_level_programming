-- Number of shows by genre
SELECT name AS genre, COUNT(t.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres t
ON id = t.genre_id
GROUP BY t.genre_id, name
HAVING COUNT(t.show_id) > 0
ORDER BY number_of_shows DESC;
