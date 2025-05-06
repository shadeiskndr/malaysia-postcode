import sqlite3

SRC_DB = "malaysia_postcode.sqlite"
DST_DB = "malaysia_postcode_distinct.sqlite"

# Connect to source and destination databases
src_conn = sqlite3.connect(SRC_DB)
dst_conn = sqlite3.connect(DST_DB)

src_cur = src_conn.cursor()
dst_cur = dst_conn.cursor()

# Create the new table in the destination database
dst_cur.execute("""
    CREATE TABLE IF NOT EXISTS postcode (
        postcode TEXT,
        town TEXT,
        state_code TEXT
    )
""")

# Select distinct rows from the source
src_cur.execute("""
    SELECT DISTINCT postcode, town, state_code
    FROM postcode
""")
rows = src_cur.fetchall()

# Insert into the destination table
dst_cur.executemany(
    "INSERT INTO postcode (postcode, town, state_code) VALUES (?, ?, ?)",
    rows
)

dst_conn.commit()
src_conn.close()
dst_conn.close()

print(f"Exported {len(rows)} distinct rows to {DST_DB}")
