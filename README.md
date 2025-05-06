# Malaysia Postcode & State Data

This project provides a CSV, JSON and SQLite database containing Malaysian postcode and state data, extracted from the original SQL source file `Malaysia_Postcode.sql`.

## Features

- **Postcode Table**: Contains Malaysian postcode data, including area names, post office/city, and state codes.
- **State Table**: Contains state codes and full state names for all Malaysian states and federal territories.
- **Python Import Scripts**: Utilities to parse the original SQL and populate a SQLite database with clean, deduplicated data.
- **Export Utilities**: Scripts to export the distinct postcode data to CSV, JSON and SQLite for easy integration with external databases.

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

## Usage

### 1. Importing Postcode Data

To extract postcode data from `Malaysia_Postcode.sql` and insert it into a SQLite database:

```bash
python3 import_postcode_sqlite.py
```

This will create `malaysia_postcode.sqlite` with the full postcode table.

### 2. Creating a Distinct Postcode Table

To create a new SQLite database containing only distinct combinations of postcode, town, and state_code (removing area_name duplicates):

```bash
python3 export_distinct_postcode_to_sqlite.py
```

This will create `malaysia_postcode_distinct.sqlite` with a deduplicated `postcode` table.

**Note:**  
The deduplicated table in `malaysia_postcode_distinct.sqlite` has the following columns:

| Column     | Type | Description         |
| ---------- | ---- | ------------------- |
| postcode   | TEXT | 5-digit postcode    |
| town       | TEXT | Town name           |
| state_code | TEXT | 3-letter state code |

### 3. Creating State Table

To create and insert Malaysia states data into the `state` table and export to SQLite, CSV, and JSON format:

```bash
python3 import_state_table.py
```

### 4. Exporting Distinct Postcode Data for External Databases

To allow other external databases or systems to access the distinct postcode data, you can export the data from `malaysia_postcode_distinct.sqlite` to a common format such as CSV or JSON.

#### Export as CSV

Use the following script to export the distinct postcode data to a CSV file:

```bash
python3 export_distinct_postcode_to_csv.py
```

This will create `malaysia_postcode_distinct.csv`, which can be imported into most external databases.

#### Export as JSON

Use the following script to export the distinct postcode data to a JSON file:

```bash
python3 export_distinct_postcode_to_json.py
```

This will create `malaysia_postcode_distinct.json`, suitable for web APIs or NoSQL databases.

Alternatively, you can share the `malaysia_postcode_distinct.sqlite` file directly if the external system supports SQLite.

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

## Requirements

- Python 3.x
- Standard library only (`sqlite3`, `re`, `csv`, `json`)
