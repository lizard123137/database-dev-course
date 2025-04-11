def init_user_likes(db):
    print("Initializing user_likes collection...")

    user_likes = db["user_likes"]
    user_likes.insert_many([
        { "_id": 1, "user_id": 1, "offer_id": 1 },
        { "_id": 2, "user_id": 2, "offer_id": 2 },
        { "_id": 3, "user_id": 3, "offer_id": 3 },
        { "_id": 4, "user_id": 4, "offer_id": 4 },
        { "_id": 5, "user_id": 5, "offer_id": 5 },
        { "_id": 6, "user_id": 6, "offer_id": 6 },
        { "_id": 7, "user_id": 7, "offer_id": 7 },
        { "_id": 8, "user_id": 8, "offer_id": 8 },
        { "_id": 9, "user_id": 9, "offer_id": 9 },
        { "_id": 10, "user_id": 10, "offer_id": 1 }
    ])
