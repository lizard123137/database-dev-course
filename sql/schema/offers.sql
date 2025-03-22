CREATE TABLE offers (
    id SERIAL PRIMARY KEY,
    
    user_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    
    price INT NOT NULL,
    description TEXT,
    status VARCHAR(100) NOT NULL,

    color VARCHAR(100),
    milage INT NOT NULL,
    vin VARCHAR(100) NOT NULL,
    condition VARCHAR(100) NOT NULL,

    created_at TIMESTAMP DEFAULT NOW(),
    modified_at TIMESTAMP,

    CONSTRAINT fk_users FOREIGN KEY(user_id) REFERENCES users(id),
    CONSTRAINT fk_vehicles FOREIGN KEY(vehicle_id) REFERENCES vehicles(id)
);