# Name
Natali Rozin (JHED ID: nrozin1)

# Module Info
**Module 4:** Testing & Documentation

**Assignment:** Pytest and Sphinx

**Due Date:** 17/06/2025

# Approach
This project simulates a pizza order: It prompts the user for crust type, sauce(s) and topping(s), prints the order and accepts payment. Each module is validated with unit tests, and the whole program flow is validated with an integration test.

The solution is designed around three core components — database connection and loading, querying, and web rendering — each encapsulated in dedicated modules to ensure easy maintainability and clarity.

1. Database Connection (`DB/connection.py`):
   - Provides a `get_db_connection()` function that establishes and returns a connection to the PostgreSQL database using psycopg.

   - Configuration details such as host, database name, user credentials, and port are defined within this module.

   - Errors during connection attempts are caught and printed, returning None if a connection cannot be established.

2. Data Loading (`DB/load_data.py`):
   - This class is responsible for reading applicant data from a JSON file and loading it into a PostgreSQL database.

   - When initializing the class, it establishes a DB connection and defines the path to the JSON file that contains the data to be loaded.

   - `create_table()` creates a new DB table named `applicants` with specified columns if it doesn’t exist, using a SQL CREATE TABLE IF NOT EXISTS statement.

   - `load_data()` reads and parses the JSON file, representing applicants records.

   - `insert_to_table(data)` inserts records into the database only if the table is empty, preventing duplicate entries. It first checks the table’s row count and proceeds with insertion only if no records exist.

   - `run_loader()` a function that puts everything together, ensuring the data is loaded and the table is ready.

   - Error handling and closing connections are included.

3. Querying (`DB/query_data.py`)
   - The Query class handles different SQL queries to analyze the applicants’ data stored in the database.

   - On instantiation, it opens a database connection for running queries.

   - Key methods include:
      - `count_fall25_entries()` — Counts applicants for the Fall 2025 term.
      - `international_percentage()` — Computes the percentage of international applicants.
      - `average_scores_international_fall25()` — Computes average GPA and GRE scores for international Fall 2025 applicants.
      - `average_gpa_american_fall25()` — Computes average GPA of American Fall 2025 applicants.
      - `accepted_fall25_percentage` — Computes the percentage of accepted applicants for Fall 2025.
      - `average_gpa_accepted_fall25()` — Computes average GPA among accepted Fall 2025 applicants.
      - `count_jhu_cs_masters()` — Counts Johns Hopkins University Computer Science Master’s applicants.
   
   - Error handling is included.

4. Flask Web Application (`app.py`)
- Defines the Flask app function create_app() that sets up the web app.

- The root route / performs these steps:
   - Calls run_loader() to ensure the database table exists and data is loaded from the JSON file if empty.
   - Instantiates a Query object to retrieve analysis results.
   - Passes the results to the index.html template for rendering.

Additional Notes:
- The data loading process is designed to avoid duplicates by checking if data already exists before inserting new records.

- This project assumes a local PostgreSQL instance configured with the credentials specified in connection.py.

# How to Run
**Step 1:** Make sure you have **Python 3.0+** installed.

**Step 2:** Install the project dependencies by running:
```bash
pip install -r requirements.txt
```

**Step 3: Update the database password** in `DB/connection.py` to match your local PostgreSQL setup.

**Step 4:** Navigate to the project directory and execute:
```bash
python app.py
```

**Step 5:** Open your browser and go to http://127.0.0.1:8000 to see the website.