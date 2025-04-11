import pymongo

from vehicles import init_vehicles
from users import init_users
from offers import init_offers
from user_likes import init_user_likes

client = pymongo.MongoClient("mongodb://localhost:27017/")

print("Creating database...")
database = client["car-trading"]

print("Initializing data...")
init_vehicles(database)
init_users(database)
init_offers(database)
init_user_likes(database)