def init_users(db):
    print("Initializing users collection...")

    users = db["users"]
    users.insert_many([
        {
            "_id": 1,
            "email": "john.doe@example.com",
            "username": "johndoe",
            "password": "d41d8cd98f00b204e9800998ecf8427e",
            "user_details": {
                "avatar": "https://media.1815.io/topgear/i/full/2021/05/bmw-m3-compact-e36-4-scaled-e1621590187123.jpg",
                "description": "Drift enthusiast and car builder."
            },
            "user_stats": {
                "cars_sold": 3,
                "cars_bought": 5
            },
            "created_at": "2025-03-29 09:50:00",
            "modified_at": None
        },
        {
            "_id": 2,
            "email": "jane.smith@example.com",
            "username": "janesmith",
            "password": "098f6bcd4621d373cade4e832627b4f6",
            "user_details": {
                "avatar": "https://www.classix.se/images/cars/2023/bmwm3estoril/till-salu-bmw-m3-e36.jpg",
                "description": "Loves JDM cars and track days."
            },
            "user_stats": {
                "cars_sold": 10,
                "cars_bought": 2
            },
            "created_at": "2025-03-29 09:51:00",
            "modified_at": None
        },
        {
            "_id": 3,
            "email": "bob.jones@example.com",
            "username": "bobjones",
            "password": "e99a18c428cb38d5f260853678922e03",
            "user_details": {
                "avatar": None,
                "description": "Weekend drifter, full-time mechanic."
            },
            "user_stats": {
                "cars_sold": 1,
                "cars_bought": 4
            },
            "created_at": "2025-03-29 09:52:00",
            "modified_at": None
        },
        {
            "_id": 4,
            "email": "mary.jane@example.com",
            "username": "maryjane",
            "password": "ab56b4d92b40713acc5af89985d4b786",
            "user_details": {
                "avatar": None,
                "description": "Aspiring Formula Drift driver."
            },
            "user_stats": {
                "cars_sold": 6,
                "cars_bought": 3
            },
            "created_at": "2025-03-29 09:53:00",
            "modified_at": None
        },
        {
            "_id": 5,
            "email": "alice.cooper@example.com",
            "username": "alicecooper",
            "password": "9a0364b9e99bb480dd25e1f0284c8555",
            "user_details": {
                "avatar": "https://i.ebayimg.com/images/g/ozYAAOSwNRdX~K68/s-l1200.jpg",
                "description": "Classic BMW collector and tuner."
            },
            "user_stats": {
                "cars_sold": 8,
                "cars_bought": 7
            },
            "created_at": "2025-03-29 09:54:00",
            "modified_at": None
        },
        {
            "_id": 6,
            "email": "richard.roe@example.com",
            "username": "richardroe",
            "password": "1d2d2a8dbd4bc1b5a33f59571b5cfb29",
            "user_details": {
                "avatar": "https://example.com/avatar6.jpg",
                "description": "Passionate about grassroots drifting."
            },
            "user_stats": {
                "cars_sold": 2,
                "cars_bought": 6
            },
            "created_at": "2025-03-29 09:55:00",
            "modified_at": None
        },
        {
            "_id": 7,
            "email": "elizabeth.green@example.com",
            "username": "elizabethgreen",
            "password": "5d41402abc4b2a76b9719d911017c592",
            "user_details": {
                "avatar": "https://www.nissan-global.com/EN/HERITAGE_COLLECTION/img/modelDetail/uploader/data/en/Web/1317164314611090367.jpg",
                "description": "Owns an S13 with an SR20 swap."
            },
            "user_stats": {
                "cars_sold": 5,
                "cars_bought": 1
            },
            "created_at": "2025-03-29 09:56:00",
            "modified_at": None
        },
        {
            "_id": 8,
            "email": "george.white@example.com",
            "username": "georgewhite",
            "password": "c4ca4238a0b923820dcc509a6f75849b",
            "user_details": {
                "avatar": None,
                "description": "Builds and sells drift car parts."
            },
            "user_stats": {
                "cars_sold": 7,
                "cars_bought": 2
            },
            "created_at": "2025-03-29 09:57:00",
            "modified_at": None
        },
        {
            "_id": 9,
            "email": "steve.martin@example.com",
            "username": "stevemartin",
            "password": "202cb962ac59075b964b07152d234b70",
            "user_details": {
                "avatar": "https://www.drifted.com/wp-content/uploads/2021/04/initial-d-ae86-thumbnail.jpg",
                "description": "Loves mountain touge runs."
            },
            "user_stats": {
                "cars_sold": 4,
                "cars_bought": 5
            },
            "created_at": "2025-03-29 09:58:00",
            "modified_at": None
        },
        {
            "_id": 10,
            "email": "susan.lee@example.com",
            "username": "susanlee",
            "password": "c81e728d9d4c2f636f067f89cc14862c",
            "user_details": {
                "avatar": "https://i.ytimg.com/vi/BQfzRp-L_oc/maxresdefault.jpg",
                "description": "Races in local drift competitions."
            },
            "user_stats": {
                "cars_sold": 9,
                "cars_bought": 3
            },
            "created_at": "2025-03-29 09:59:00",
            "modified_at": None
        }
    ])