
  CREATE TABLE passengers(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights2
); 

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Maria', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Dave', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Jen', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Ali', 4);