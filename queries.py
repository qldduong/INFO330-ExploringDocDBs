import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters
import json # Idk if I'm supposed to be doing this 
from pymongo import MongoClient
# Location: C:\Users\renti\Documents\INFO330\INFO330-ExploringDocDBs

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']



# Write a query that returns all the Pokemon named "Pikachu". (1pt)
def find_pikachu():
    return (pokemonColl.find_one({"name":"Pikachu"}))
query_1_result = find_pikachu()

# Run this code if you want to see the results of power_query:
#print(query_1_result)

###############################################################################################

# Write a query that returns all the Pokemon with an attack greater than 150. (1pt)


def power_query():
    power_set = (pokemonColl.find( { "attack": { "$gt": 150 } } ))
    for pokemon in power_set:
        print(pokemon)

# Run this code if you want to see the results of power_query:
#power_query() 

###############################################################################################


# Write a query that returns all the Pokemon with an ability of "Overgrow" (1pt)
def ability_query():
    overgrow_set = pokemonColl.find({"abilities": "Overgrow"})
    ohohohoh_set = pokemonColl.find({ "tags": "Overgrow" } )

    for pokemon in overgrow_set:
        print(pokemon)

# Run this code if you want to see the results of ability_query:
ability_query()