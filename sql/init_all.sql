\echo 'Loading schema...'
\i /docker-entrypoint-initdb.d/schema/user_details.sql
\i /docker-entrypoint-initdb.d/schema/user_stats.sql
\i /docker-entrypoint-initdb.d/schema/users.sql
\i /docker-entrypoint-initdb.d/schema/manufacturers.sql
\i /docker-entrypoint-initdb.d/schema/vehicles.sql
\i /docker-entrypoint-initdb.d/schema/offers.sql
\i /docker-entrypoint-initdb.d/schema/user_likes.sql



\echo 'Loading initial data...'
COPY manufacturers(id,name)
FROM '/docker-entrypoint-initdb.d/data/manufacturers.csv'
DELIMITER ','
CSV HEADER;
SELECT setval('manufacturers_id_seq', (SELECT MAX(id) FROM manufacturers));

COPY vehicles(id,manufacturer_id,model,generation,horse_power,left_hand_drive,driven_wheels,transmission,body_style)
FROM '/docker-entrypoint-initdb.d/data/vehicles.csv'
DELIMITER ','
CSV HEADER;
SELECT setval('vehicles_id_seq', (SELECT MAX(id) FROM vehicles));

COPY user_details(id,avatar,description)
FROM '/docker-entrypoint-initdb.d/data/user_details.csv'
DELIMITER ','
CSV HEADER;
SELECT setval('user_details_id_seq', (SELECT MAX(id) FROM user_details));

COPY user_stats(id,cars_sold,cars_bought)
FROM '/docker-entrypoint-initdb.d/data/user_stats.csv'
DELIMITER ','
CSV HEADER;
SELECT setval('user_stats_id_seq', (SELECT MAX(id) FROM user_stats));

COPY users(id,email,username,password,user_details_id,user_stats_id,created_at,modified_at)
FROM '/docker-entrypoint-initdb.d/data/users.csv'
DELIMITER ','
CSV HEADER;
SELECT setval('users_id_seq', (SELECT MAX(id) FROM users));

COPY offers(id,user_id,vehicle_id,price,description,status,color,milage,vin,condition,created_at,modified_at)
FROM '/docker-entrypoint-initdb.d/data/offers.csv'
DELIMITER ','
CSV HEADER;
SELECT setval('offers_id_seq', (SELECT MAX(id) FROM offers));

COPY user_likes(id,user_id,offer_id)
FROM '/docker-entrypoint-initdb.d/data/user_likes.csv'
DELIMITER ','
CSV HEADER;
SELECT setval('user_likes_id_seq', (SELECT MAX(id) FROM user_likes));



\echo 'Example Queries:'
\echo ' - DML Queries:'
INSERT INTO manufacturers(name) VALUES ('volvo');
UPDATE manufacturers SET name = 'Volvo' WHERE name = 'volvo';

INSERT INTO manufacturers(name) VALUES ('test');
DELETE FROM manufacturers WHERE name = 'test';