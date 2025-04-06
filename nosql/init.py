import pymongo

from vehicles import init_vehicles

client = pymongo.MongoClient("mongodb://localhost:27017/")

print("Creating database...")
database = client["car-trading"]

print("Initializing data...")
init_vehicles(database)