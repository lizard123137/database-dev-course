CREATE TABLE user_stats (
    id SERIAL PRIMARY KEY,
    cars_sold INTEGER NOT NULL DEFAULT 0,
    cars_bought INTEGER NOT NULL DEFAULT 0
);