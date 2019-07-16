-- list all records of a table
SELECT score, name FROM second_table WHERE EXISTS (SELECT name) ORDER BY score DESC;
