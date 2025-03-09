CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(100) NOT NULL,
    password TEXT NOT NULL,
    user_stats_id INT NOT NULL,
    
    created_at TIMESTAMP DEFAULT NOW(),
    modified_at TIMESTAMP,

    CONSTRAINT fk_user_stats FOREIGN KEY(user_stats_id) REFERENCES user_stats(id)
);