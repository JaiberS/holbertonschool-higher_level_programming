-- Show genre from a show
SELECT DISTINCT tv_genres.name FROM tv_genres, tv_shows, tv_show_genres WHERE tv_genres.id=tv_show_genres.genre_id and tv_show_genres.show_id = 8 ORDER BY tv_genres.name ASC;
