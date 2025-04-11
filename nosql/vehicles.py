def init_vehicles(db):
    print("Initializing vehicles collection...")

    vehicles = db["vehicles"]
    vehicles.insert_many([
        {
            "_id": 1,
            "manufacturer": "BMW",
            "model": "E36 328i",
            "generation": 3,
            "horse_power": 193,
            "left_hand_drive": True,
            "driven_wheels": "RWD",
            "transmission": "Manual",
            "body_style": "Coupe"
        },
        {
            "_id": 2,
            "manufacturer": "BMW",
            "model": "E46 330Ci",
            "generation": 4,
            "horse_power": 231,
            "left_hand_drive": True,
            "driven_wheels": "RWD",
            "transmission": "Manual",
            "body_style": "Coupe"
        },
        {
            "_id": 3,
            "manufacturer": "BMW",
            "model": "E39 540i",
            "generation": 4,
            "horse_power": 286,
            "left_hand_drive": True,
            "driven_wheels": "RWD",
            "transmission": "Manual",
            "body_style": "Sedan"
        },
        {
            "_id": 4,
            "manufacturer": "BMW",
            "model": "E36 M3",
            "generation": 3,
            "horse_power": 321,
            "left_hand_drive": True,
            "driven_wheels": "RWD",
            "transmission": "Manual",
            "body_style": "Coupe"
        },
        {
            "_id": 5,
            "manufacturer": "BMW",
            "model": "E46 M3",
            "generation": 4,
            "horse_power": 343,
            "left_hand_drive": True,
            "driven_wheels": "RWD",
            "transmission": "Manual",
            "body_style": "Coupe"
        },
        {
            "_id": 6,
            "manufacturer": "Nissan",
            "model": "350Z",
            "generation": 1,
            "horse_power": 287,
            "left_hand_drive": True,
            "driven_wheels": "RWD",
            "transmission": "Manual",
            "body_style": "Coupe"
        },
        {
            "_id": 7,
            "manufacturer": "Nissan",
            "model": "S13 240SX",
            "generation": 1,
            "horse_power": 155,
            "left_hand_drive": True,
            "driven_wheels": "RWD",
            "transmission": "Manual",
            "body_style": "Coupe"
        },
        {
            "_id": 8,
            "manufacturer": "Opel",
            "model": "Omega",
            "generation": 2,
            "horse_power": 204,
            "left_hand_drive": True,
            "driven_wheels": "RWD",
            "transmission": "Manual",
            "body_style": "Sedan"
        },
        {
            "_id": 9,
            "manufacturer": "Fiat",
            "model": "124 Spider",
            "generation": 1,
            "horse_power": 170,
            "left_hand_drive": True,
            "driven_wheels": "RWD",
            "transmission": "Manual",
            "body_style": "Convertible"
        },
        {
            "_id": 10,
            "manufacturer": "Toyota",
            "model": "GT86",
            "generation": 1,
            "horse_power": 205,
            "left_hand_drive": True,
            "driven_wheels": "RWD",
            "transmission": "Manual",
            "body_style": "Coupe"
        }
    ])