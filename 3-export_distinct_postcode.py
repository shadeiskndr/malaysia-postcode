import sqlite3
import csv
import json

SRC_DB = "malaysia_postcode.sqlite"
DST_DB = "malaysia_postcode_distinct.sqlite"
CSV_FILE = "malaysia_postcode_distinct.csv"
JSON_FILE = "malaysia_postcode_distinct.json"

def fetch_distinct_postcodes():
    conn = sqlite3.connect(SRC_DB)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT postcode, town, state_code FROM postcode")
    rows = cur.fetchall()
    conn.close()
    return rows

def export_to_sqlite(rows):
    conn = sqlite3.connect(DST_DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS postcode (
            postcode TEXT,
            town TEXT,
            state_code TEXT
        )
    """)
    cur.execute("DELETE FROM postcode")
    cur.executemany(
        "INSERT INTO postcode (postcode, town, state_code) VALUES (?, ?, ?)",
        rows
    )
    conn.commit()
    conn.close()
    print(f"Exported {len(rows)} distinct rows to {DST_DB}")

def export_to_csv(rows):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["postcode", "town", "state_code"])
        writer.writerows(rows)
    print(f"Exported to {CSV_FILE}")

def export_to_json(rows):
    data = [dict(zip(["postcode", "town", "state_code"], row)) for row in rows]
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Exported to {JSON_FILE}")

if __name__ == "__main__":
    rows = fetch_distinct_postcodes()
    export_to_csv(rows)
    export_to_json(rows)
    export_to_sqlite(rows)
