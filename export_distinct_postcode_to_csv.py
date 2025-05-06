import sqlite3
import csv

DB = "malaysia_postcode_distinct.sqlite"
OUT_CSV = "malaysia_postcode_distinct.csv"

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("SELECT postcode, town, state_code FROM postcode")

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["postcode", "town", "state_code"])
    writer.writerows(cur.fetchall())

conn.close()
print(f"Exported to {OUT_CSV}")
