CREATE TABLE vehicles (
    id SERIAL PRIMARY KEY,

    manufacturer_id
    model VARCHAR(100) NOT NULL,
    generation INT NOT NULL,

    horse_power INT,
    left_hand_drive BOOLEAN,
    driven_wheels INT,
    transmission VARCHAR(100),
    body_style VARCHAR(100),
    
    CONSTRAINT fk_manufacturers FOREIGN KEY(manufacturer_id) REFERENCES manufacturers(id)
);