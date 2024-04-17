import requests

# Fetch the JSON data
url = "https://pokeapi.co/api/v2/pokemon/ditto/"
response = requests.get(url)
data = response.json()

# Displaying all data
print("1. Abilities:")
for ability in data['abilities']:
    print(f"   - Name: {ability['ability']['name']}")
    print(f"     URL: {ability['ability']['url']}")
    print(f"     Is Hidden: {ability['is_hidden']}")
    print(f"     Slot: {ability['slot']}")

print("\n2. Base Experience:", data['base_experience'])

print("\n3. Cries:")
print("   - Latest:", data['cries']['latest'])
print("   - Legacy:", data['cries']['legacy'])

print("\n4. Forms:")
print("   - Name:", data['forms'][0]['name'])
print("     URL:", data['forms'][0]['url'])

print("\n5. Game Indices:")
for game_index in data['game_indices']:
    print(f"   - Game Index {game_index['game_index']}:")
    print(f"     Version Name: {game_index['version']['name']}")
    print(f"     URL: {game_index['version']['url']}")

print("\n6. Height:", data['height'])

print("\n7. Held Items:")
for item in data['held_items']:
    print(f"   - Name: {item['item']['name']}")
    print(f"     URL: {item['item']['url']}")
    print("     Version Details:", item['version_details'])

print("\n8. ID:", data['id'])

print("\n9. Is Default:", data['is_default'])

print("\n10. Location Area Encounters:", data['location_area_encounters'])

print("\n11. Moves:")
for move in data['moves']:
    print(f"   - Name: {move['move']['name']}")
    print(f"     URL: {move['move']['url']}")
    print("     Version Group Details:", move['version_group_details'])

print("\n12. Name:", data['name'])

print("\n13. Order:", data['order'])

print("\n14. Species:")
print(f"    - Name: {data['species']['name']}")
print(f"      URL: {data['species']['url']}")

print("\n15. Sprites:")
for sprite in data['sprites']:
    print(f"    - {sprite}: {data['sprites'][sprite]}")

print("\n16. Stats:")
for stat in data['stats']:
    print(f"   - Base Stat {stat['stat']['name'].replace('-', ' ').title()}:")
    print(f"     Name: {stat['stat']['name']}")
    print(f"     URL: {stat['stat']['url']}")
    print(f"     Base Stat: {stat['base_stat']}")
    print(f"     Effort: {stat['effort']}")

print("\n17. Types:")
for poke_type in data['types']:
    print(f"   - Slot {poke_type['slot']}:")
    print(f"     Name: {poke_type['type']['name']}")
    print(f"     URL: {poke_type['type']['url']}")

print("\n18. Weight:", data['weight'])
