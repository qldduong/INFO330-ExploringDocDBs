import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters
import json # Idk if I'm supposed to be doing this 
from pymongo import MongoClient
# Location: C:\Users\renti\Documents\INFO330\INFO330-ExploringDocDBs

# Connecting to MongoDB with code provided
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']


connection = sqlite3.connect("pokemon.sqlite")
cursor = connection.cursor()

# Not sure how to get names / types as just strings and as tuples
# This method cleans tuple items up for readability
def cleaning(string_to_clean):
    string_to_clean = string_to_clean.strip("(")
    string_to_clean = string_to_clean.strip(")")
    string_to_clean = string_to_clean.strip(",")
    string_to_clean = string_to_clean.strip("'")
    return(string_to_clean)


# SQLITE query that tells how many pokemon there are in the pokemon table
pok_count_sql = "SELECT COUNT(name) FROM pokemon"
pok_count_results = cursor.execute(pok_count_sql)
pok_count = pok_count_results.fetchall()
pok_count = cleaning(str(pok_count[0]))
pok_count = int(pok_count)

curr_pok = 1


while curr_pok <= pok_count: 
    curr_list = []

    # Getting the name of each pokemon 
    name_sql = "SELECT name FROM pokemon WHERE id = ?"
    name_results = cursor.execute(name_sql, [curr_pok])
    name_list = name_results.fetchall()
    
    for name_tup in name_list:
        for name_val in name_tup:
            pok_name = name_val
            curr_list.append(name_val)

    
    # Other: pokedex_number, hp, attack, defense, speed, sp_attack, sp_defense 
    stats_sql = "SELECT pokedex_number, hp, attack, defense, speed, sp_attack, sp_defense FROM pokemon WHERE id = ?"
    stats_results = cursor.execute(stats_sql, [curr_pok])
    stats_list = stats_results.fetchall()
    
    for stat_tup in stats_list:
        for stat_val in stat_tup:
            curr_list.append(stat_val)


    # Getting the types of each pokemon 
    types = [] 
    type1_sql = "SELECT type1 FROM pokemon_types_view WHERE name = ?"
    type1_results = cursor.execute(type1_sql, [pok_name])
    type1 = type1_results.fetchall()
    type1 = str(type1[0])

    type2_sql = "SELECT type2 FROM pokemon_types_view WHERE name = ?"
    type2_results = cursor.execute(type2_sql, [pok_name])
    type2 = type2_results.fetchall()
    type2 = str(type2[0])

    type1 = cleaning(type1)
    type2 = cleaning(type2)
    types.append(type1)
    types.append(type2)
    curr_list.append(types)

    # Gathering the abilities of each pokemon
    abilities = []
    abilities_sql = "SELECT ability.name FROM ability, pokemon_abilities WHERE id = ability_id AND pokemon_id = ?"
    abilities_results = cursor.execute(abilities_sql, [curr_pok])
    abilities_fetch = abilities_results.fetchall()

    
    for abil_tup in abilities_fetch:
        for abil in abil_tup:
            abilities.append(abil)
    curr_list.append(abilities)
    
    # Execute this line to check the format of the lists being converted into documents: 
    # print(curr_list)

    # Increment the curr_pok counter
    curr_pok +=1

    # Curr_list[]
    # [name, pokedex_number, hp, attack, defense, speed, sp_attack, sp_defense, types, abilities]
    
    # Okay, but what about the JSON? 
    pokemon = {
        "name": curr_list[0],
        "pokedex_number": curr_list[1],
        "hp": curr_list[2],
        "attack": curr_list[3],
        "defense": curr_list[4],
        "speed": curr_list[5],
        "sp_attack": curr_list[6],
        "sp_defense": curr_list[7],
        "types": curr_list[8],
        "abilities": curr_list[9]
    }
    pokemonColl.insert_one(pokemon)









