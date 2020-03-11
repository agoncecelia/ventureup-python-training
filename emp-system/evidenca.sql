CREATE TABLE evidenca(
	id serial primary key,
	p_id int references puntor(id),
	check_in timestamp,
	check_out timestamp
);
