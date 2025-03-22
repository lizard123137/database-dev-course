CREATE TABLE user_likes (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    offer_id INT NOT NULL,
    
    CONSTRAINT fk_users FOREIGN KEY(user_id) REFERENCES users(id),
    CONSTRAINT fk_offers FOREIGN KEY(offer_id) REFERENCES offers(id)
);