/*
  CREATE TABLE flights2(
    id SERIAL PRIMARY KEY,
   origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
); 
*/
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 420);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Boston', 200);
INSERT INTO flights (origin, destination, duration) VALUES ('Tokyo', 'Dubai', 540);
INSERT INTO flights (origin, destination, duration) VALUES ('Dubai', 'Doha', 80);
INSERT INTO flights (origin, destination, duration) VALUES ('Dubai', 'Moscow', 240);
INSERT INTO flights (origin, destination, duration) VALUES ('Dubai', 'Islamabad', 340);
INSERT INTO flights (origin, destination, duration) VALUES ('Manila', 'Dubai', 560);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Dubai', 520);
INSERT INTO flights (origin, destination, duration) VALUES ('Dubai', 'London', 410);