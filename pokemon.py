# making api request using python and printing the output.

import requests

while True:
    ask = input("Please enter the Pokemon name?\n").lower()
    baseURL = f"https://pokeapi.co/api/v2/pokemon/{ask}" 

    req = requests.get(baseURL)

    if req.status_code == 200:
        pokemon = req.json()
        print(f"Name: {ask}")
        print(f"Weight: {pokemon['weight']}kg")
        print(f"Height: {pokemon['height']}ft")

        print("Abilities: ")
        for abilities in pokemon['abilities']:
            print(abilities['ability']['name'])

        # same as abilities above
        # print("Moves: ")
        # for moves in pokemon['moves']:
        #     print(moves['move']['name'])

    else:
        print("Pokemon not found!")