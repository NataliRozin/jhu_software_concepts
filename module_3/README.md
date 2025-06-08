# Name
Natali Rozin (JHED ID: nrozin1)

# Module Info
**Module 3:** Web Scraping

**Assignment:** Databases

**Due Date:** 08/06/2025

# Approach
This project implements a Flask web application that loads applicant data from a local JSON file into a PostgreSQL database and queries various statistics to display on a dynamic web page.

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

Additional Notes:
- The main.py script acts as the entry point, coordinating the workflow by instantiating the scraper, requesting data for a large number of pages (targeting 10,000+ entries), passing raw data through cleaning, and finally saving the results.

- The entire codebase sticks closely to the Module 2 assignment guidelines by relying only on urllib3, BeautifulSoup, regex, json, and Python’s built-in libraries.

- The scraper follows ethical scraping practices by respecting the robots.txt rules.

- The design is flexible and easy to update, allowing easy adjustments to the number of pages scraped or addition of new data fields in future iterations.

# How to Run
**Step 1:** Make sure you have **Python 3.0+** installed.

**Step 2:** Install the project dependencies by running:
```bash
pip install -r requirements.txt
```

**Step 3:** Navigate to the project directory and execute:
```bash
python app.py
```

**Step 4:** Open your browser and go to http://127.0.0.1:8000 to see the website.