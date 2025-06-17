# Name
Natali Rozin (JHED ID: nrozin1)

# Module Info
**Module 5:** Code Assurance & Security

**Assignment:** Software Assurance, Static Code Analysis, and SQL Injections

**Due Date:** 17/06/2025

# Approach
This repository contains the updated codebase from Module 3, with improvements focused on code quality, SQL injection defenses, and dependency visualization.

1. Code linting (quality):
   Iteratively ran pylint on all files and addressed every warning and error by:
   - Fixing formatting issues (indentation, line length, spacing).
   - Renaming variables and functions for clarity and consistency.
   - Adding or improving docstrings and comments.
   - Removing unused imports and redundant code.
   - Reducing the number of attributes passed to functions to improve readability and maintainability, making functions simpler and more focused.

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