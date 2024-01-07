-- Lists shows with at least one genre linked
SELECT title, tv_show_genres.genre_id 
FROM tv_shows 
JOIN tv_show_genres 
ON genre_id =  tv_show_genres.genre_id
ORDER BY title ASC, tv_show_genres.genre_id ASC;
