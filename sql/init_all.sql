\echo 'Loading schema...'
\i schema/user_stats.sql
\i schema/users.sql
\i schema/manufacturers.sql

\echo 'Loading initial data...'
COPY manufacturers(name)
FROM 'data/manufacturers.csv'
DELIMITER ','
CSV HEADER;