import json

# Convert states.json to SQL
with open('states.json', 'r', encoding='utf-8') as f:
    states = json.load(f)

with open('states_data.sql', 'w', encoding='utf-8') as f:
    for state in states:
        state_code = state['state_code'].replace("'", "''")
        state_name = state['state_name'].replace("'", "''")
        f.write(
            f"INSERT INTO states (state_code, state_name) VALUES ('{state_code}', '{state_name}') ON DUPLICATE KEY UPDATE state_name=VALUES(state_name);\n"
        )

# Convert malaysia_postcode_distinct.json to SQL
with open('malaysia_postcode_distinct.json', 'r', encoding='utf-8') as f:
    postcodes = json.load(f)

with open('postcodes_data.sql', 'w', encoding='utf-8') as f:
    for pc in postcodes:
        postcode = pc['postcode'].replace("'", "''")
        town = pc['town'].replace("'", "''")
        state_code = pc['state_code'].replace("'", "''")
        f.write(
            f"INSERT INTO postcodes (postcode, town, state_code) VALUES ('{postcode}', '{town}', '{state_code}') ON DUPLICATE KEY UPDATE town=VALUES(town), state_code=VALUES(state_code);\n"
        )

print("SQL files generated: states_data.sql, postcodes_data.sql")
