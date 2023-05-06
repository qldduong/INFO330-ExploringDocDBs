from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Original line of code: print("I found " + pokemonColl.count_documents({}) + " pokemon")

# Edited code, since I was running into a bug:
print("I found " + str((pokemonColl.count_documents({}))) + " pokemon")


