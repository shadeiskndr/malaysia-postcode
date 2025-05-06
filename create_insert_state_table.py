import sqlite3
import csv
import json

DB_FILE = "states.sqlite"

states = [
    ('JHR', 'Johor'),
    ('KDH', 'Kedah'),
    ('KTN', 'Kelantan'),
    ('KUL', 'Wilayah Persekutuan Kuala Lumpur'),
    ('LBN', 'Wilayah Persekutuan Labuan'),
    ('MLK', 'Melaka'),
    ('NSN', 'Negeri Sembilan'),
    ('PHG', 'Pahang'),
    ('PJY', 'Wilayah Persekutuan Putra Jaya'),
    ('PLS', 'Perlis'),
    ('PNG', 'Pulau Pinang'),
    ('PRK', 'Perak'),
    ('SBH', 'Sabah'),
    ('SGR', 'Selangor'),
    ('SRW', 'Sarawak'),
    ('TRG', 'Terengganu'),
]

conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS state (
        state_code TEXT PRIMARY KEY,
        state_name TEXT
    )
""")
cur.execute("CREATE INDEX IF NOT EXISTS idx_state_name ON state(state_name)")

cur.executemany(
    "INSERT OR REPLACE INTO state (state_code, state_name) VALUES (?, ?)",
    states
)

conn.commit()
conn.close()

print(f"Inserted {len(states)} rows into 'state' table in {DB_FILE}")

# --- Export to CSV ---
with open("states.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["state_code", "state_name"])
    writer.writerows(states)
print("Exported states to states.csv")

# --- Export to JSON ---
states_json = [{"state_code": code, "state_name": name} for code, name in states]
with open("states.json", "w", encoding="utf-8") as jsonfile:
    json.dump(states_json, jsonfile, ensure_ascii=False, indent=2)
print("Exported states to states.json")
