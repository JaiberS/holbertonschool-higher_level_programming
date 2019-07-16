-- show genre by show
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id FROM tv_genres, tv_show_genres, tv_shows ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
