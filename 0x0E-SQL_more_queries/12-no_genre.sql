-- lists all shows contained in hbtn_0d_tvshows without genre linked
SELECT a.title, b.genre_id FROM tv_shows a LEFT JOIN tv_show_genres b ON a.id = b.show_id WHERE b.genre_id IS NULL ORDER BY a.title ASC, b.genre_id ASC;
