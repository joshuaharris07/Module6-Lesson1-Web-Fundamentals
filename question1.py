# 1. Exploring Web Technologies and Python Programming


# Task 1: Setting Up a Python Virtual Environment and Installing Packages

# to create the virtual environment type the next line into the terminal:
    # python -m venv lesson1venv

#   to activate the virtual environment:
    # lesson1venv\scripts\activate

# to install the requests package:
    # pip install requests


# Task 2: Fetching Data from the Pokémon API
# 1. Write a Python script to make a GET request to the Pokémon API (`https://pokeapi.co/api/v2/pokemon/pikachu`).

# 2. Extract and print the name and abilities of the Pokémon.

# Expected Outcome: The script should output the name of the Pokémon (Pikachu) and a list of its abilities.

import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

json_data = response.text

pikachu_info = json.loads(json_data)

print(f"Name: {pikachu_info["name"].title()}")
print(f"{pikachu_info["name"].title()}'s abilities:")
for ability in pikachu_info["abilities"]:
    print(ability)


# Task 3: Analyzing and Displaying Data

# 1. Modify the script to fetch data for three different Pokémon.

# 2. Create a function to calculate and return the average weight of these Pokémon.

# 3. Print the names, abilities, and average weight of the three Pokémon. **Code Example:**

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    json_data = response.text
    pokemon_info = json.loads(json_data)
    return pokemon_info


def calculate_average_weight(pokemon_list):
    pokemon_count = 0
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight += pokemon["weight"]
        pokemon_count += 1
    return total_weight / pokemon_count


pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_list = []

for pokemon in pokemon_names:
    pokemon_list.append(fetch_pokemon_data(pokemon))

average_weight = format(calculate_average_weight(pokemon_list), ".2f")
print(f"The average weight of these pokemon is {average_weight}")


