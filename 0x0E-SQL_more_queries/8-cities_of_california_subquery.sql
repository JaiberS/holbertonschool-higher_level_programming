-- Select a data from another table tada
SELECT cities.id, cities.name FROM cities, states WHERE cities.state_id=states.id and states.name='California';
