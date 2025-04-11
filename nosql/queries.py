# This file is not currently used, but is an example of how you would retrieve data from the database
def query_examples(db):
    # Offers with vehicles and users
    offers = db['offers'].aggregate([
        {
            '$lookup': {
                'from': 'vehicles', 
                'localField': 'vehicle_id', 
                'foreignField': '_id', 
                'as': 'vehicle'
            }
        }, {
            '$unwind': {
                'path': '$vehicle', 
                'preserveNullAndEmptyArrays': True
            }
        }, {
            '$lookup': {
                'from': 'users', 
                'localField': 'user_id', 
                'foreignField': '_id', 
                'as': 'user'
            }
        }, {
            '$unwind': {
                'path': '$user', 
                'preserveNullAndEmptyArrays': True
            }
        }
    ])