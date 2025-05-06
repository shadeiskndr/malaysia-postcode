# Malaysia Postcode & State Data

This project provides Malaysian postcode and state data in CSV, JSON, and SQLite formats, extracted and processed from the original SQL source file `Malaysia_Postcode.sql`. It includes Python scripts to parse, deduplicate, and export the data for easy integration with other systems or databases.

---

## Features

- **Postcode Table**: Malaysian postcode data with area names, towns, and state codes.
- **State Table**: State codes and full state names for all Malaysian states and federal territories.
- **Python Scripts**: Utilities to parse the original SQL, populate SQLite databases, deduplicate data, and export to CSV, JSON, or SQL insert statements.
- **Data Exports**: Easily generate deduplicated postcode data and state data in multiple formats.

---

## Database Schema

### Table: `postcode`

| Column     | Type | Description           |
| ---------- | ---- | --------------------- |
| postcode   | TEXT | 5-digit postcode      |
| area_name  | TEXT | Area or locality name |
| town       | TEXT | Town name             |
| state_code | TEXT | 3-letter state code   |

### Table: `state`

| Column     | Type | Description              |
| ---------- | ---- | ------------------------ |
| state_code | TEXT | 3-letter state code (PK) |
| state_name | TEXT | Full state name          |

### Deduplicated Table: `postcode` (in `malaysia_postcode_distinct.sqlite`)

| Column     | Type | Description         |
| ---------- | ---- | ------------------- |
| postcode   | TEXT | 5-digit postcode    |
| town       | TEXT | Town name           |
| state_code | TEXT | 3-letter state code |

---

## Usage

### 1. Importing Postcode Data

Extract postcode data from `Malaysia_Postcode.sql` and insert it into a SQLite database:

```bash
python3 1-import_postcode_sql_to_sqlite.py
```

This creates `malaysia_postcode.sqlite` with the full postcode table.

---

### 2. Creating State Table

Create and insert Malaysia states data into the `state` table, and export to SQLite, CSV, and JSON formats:

```bash
python3 2-create_insert_state_table.py
```

This creates `states.sqlite`, `states.csv`, and `states.json`.

---

### 3. Creating a Distinct Postcode Table and Exporting Data

Generate a deduplicated postcode table (postcode, town, state_code) and export to SQLite, CSV, and JSON:

```bash
python3 3-export_distinct_postcode.py
```

This creates:

- `malaysia_postcode_distinct.sqlite` (deduplicated postcode table)
- `malaysia_postcode_distinct.csv`
- `malaysia_postcode_distinct.json`

---

### 4. Exporting Postcode and State Data to SQL Insert Statements

Convert the JSON postcode and state data into SQL insert statements for use in other SQL databases (e.g., MySQL, MariaDB):

```bash
python3 4-import_postcodes_states_to_sql.py
```

This generates:

- `states_data.sql`: SQL insert statements for the states table.
- `postcodes_data.sql`: SQL insert statements for the postcodes table.

---

## Example Queries

- **Get all postcodes for a state:**

  ```sql
  SELECT postcode, town FROM postcode WHERE state_code = 'SGR';
  ```

- **Join postcode with state name:**

  ```sql
  SELECT p.postcode, p.town, s.state_name
  FROM postcode p
  JOIN state s ON p.state_code = s.state_code;
  ```

---

## Requirements

- Python 3.x
- Standard library only (`sqlite3`, `re`, `csv`, `json`)

---

## File Overview

| Script/File                         | Purpose                                              |
| ----------------------------------- | ---------------------------------------------------- |
| 1-import_postcode_sql_to_sqlite.py  | Parse SQL and import postcode data into SQLite       |
| 2-create_insert_state_table.py      | Create/insert state data, export to SQLite/CSV/JSON  |
| 3-export_distinct_postcode.py       | Deduplicate postcode data, export to SQLite/CSV/JSON |
| 4-import_postcodes_states_to_sql.py | Convert JSON data to SQL insert statements           |
| Malaysia_Postcode.sql               | Original postcode SQL data                           |
| malaysia_postcode.sqlite            | Full postcode SQLite database                        |
| malaysia_postcode_distinct.sqlite   | Deduplicated postcode SQLite database                |
| malaysia_postcode_distinct.csv      | Deduplicated postcode data (CSV)                     |
| malaysia_postcode_distinct.json     | Deduplicated postcode data (JSON)                    |
| states.sqlite                       | State data (SQLite)                                  |
| states.csv                          | State data (CSV)                                     |
| states.json                         | State data (JSON)                                    |
| states_data.sql                     | State data (SQL insert statements)                   |
| postcodes_data.sql                  | Postcode data (SQL insert statements)                |

---

## Project Structure

All scripts and data files are in the project root. For larger projects, consider organizing into `scripts/`, `data/`, and `db/` folders.

---

## License

MIT License (or specify your license here)
