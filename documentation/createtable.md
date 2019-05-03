# CREATE TABLE- Lauseet

CREATE TABLE account (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	roles VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE location (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	price INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)

CREATE TABLE suggestion (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	whenis DATE NOT NULL, 
	location_id INTEGER NOT NULL, 
	success BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(location_id) REFERENCES location (id), 
	CHECK (success IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)

CREATE TABLE vote (
	id INTEGER NOT NULL, 
	suggestion_id INTEGER, 
	account_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(suggestion_id) REFERENCES suggestion (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)
