import sqlite3
import json

DB = "malaysia_postcode_distinct.sqlite"
OUT_JSON = "malaysia_postcode_distinct.json"

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("SELECT postcode, town, state_code FROM postcode")
rows = [dict(zip(["postcode", "town", "state_code"], row)) for row in cur.fetchall()]

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

conn.close()
print(f"Exported to {OUT_JSON}")
