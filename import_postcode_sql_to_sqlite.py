import sqlite3
import re

SQL_FILE = "Malaysia_Postcode.sql"
DB_FILE = "malaysia_postcode.sqlite"

# 1. Extract INSERT values from the SQL file
insert_values = []
insert_pattern = re.compile(r"INSERT INTO `postcode` VALUES (.+);", re.DOTALL)

with open(SQL_FILE, "r", encoding="utf-8") as f:
    content = f.read()
    matches = insert_pattern.findall(content)
    for match in matches:
        rows = re.findall(r"\(([^)]+)\)", match)
        for row in rows:
            # This splits correctly on ',' between quoted strings
            fields = [x.strip().strip("'") for x in re.split(r"','", row.strip("'"))]
            if len(fields) == 4:
                insert_values.append(fields)


# 2. Create SQLite database and table
conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS postcode (
        postcode TEXT,
        area_name TEXT,
        town TEXT,
        state_code TEXT
    )
""")

# 3. Insert data
cur.executemany(
    "INSERT INTO postcode (postcode, area_name, town, state_code) VALUES (?, ?, ?, ?)",
    insert_values
)
conn.commit()
conn.close()
print(f"Inserted {len(insert_values)} rows into {DB_FILE}")
