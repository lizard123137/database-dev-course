\echo 'Loading schema...'
\i /docker-entrypoint-initdb.d/schema/user_details.sql
\i /docker-entrypoint-initdb.d/schema/user_stats.sql
\i /docker-entrypoint-initdb.d/schema/users.sql
\i /docker-entrypoint-initdb.d/schema/manufacturers.sql
\i /docker-entrypoint-initdb.d/schema/vehicles.sql
\i /docker-entrypoint-initdb.d/schema/offers.sql
\i /docker-entrypoint-initdb.d/schema/user_likes.sql

\echo 'Loading initial data...'
COPY manufacturers(name)
FROM '/docker-entrypoint-initdb.d/data/manufacturers.csv'
DELIMITER ','
CSV HEADER;