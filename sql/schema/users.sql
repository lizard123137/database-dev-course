CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    modified_at TIMESTAMP
);