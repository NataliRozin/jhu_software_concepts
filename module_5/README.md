# Name
Natali Rozin (JHED ID: nrozin1)

# Module Info
**Module 5:** Code Assurance & Security

**Assignment:** Software Assurance, Static Code Analysis, and SQL Injections

**Due Date:** 17/06/2025

# Approach
This repository contains the updated codebase from Module 3, with improvements focused on code quality, SQL injection defenses, and dependency visualization.

**1. Code linting (quality):**

   - `pylint` was run iteratively on all files, and all warnings and errors were addressed by:

      - Fixing formatting issues such as indentation, line length, and spacing.
      - Renaming variables and functions to improve clarity and consistency.
      - Addin docstrings and comments.
      - Removing unused imports and redundant code.
      - Reducing the number of parameters passed to functions to improve readability and maintainability.

   - All files were linted until a perfect score of 10/10 was achieved with no remaining errors or warnings.

   - A `.pylintrc` configuration file is included to suppress known false positives:
      ```bash
      generated-members=cursor,commit,close
      ```
      This resolved issues where `pylint` incorrectly flagged database connection members (e.g., `cursor`, `commit`, `close`), as missing. These were false positives caused by `pylint`'s static analysis, which does not evaluate runtime states such as closed connections.

**2. Securing SQL Statements:**
   - All SQL queries were refactored using `psycopg`’s SQL composition API:

      - Used `sql.SQL()` to build queries safely.
      - Used `sql.Identifier()`, `sql.Literal()`, and `sql.placeholders` to securely insert table names, column names, and values.
      - Separated query definition from execution for improved clarity and safety.
   
   - Explicit `LIMIT` clauses were added to all `SELECT` statements to prevent large or unintended data retrieval.


**3. Dependency Graph Generation:**
 - A module-level dependency graph of `app.py` was generated using `pydeps` and `graphviz` to visualize and analyze code structure.

**4. Environment Management:**
 - A local Python virtual environment (not included in the repository) was used to install dependencies and test the codebase, ensuring consistent and isolated runtime behavior.

# How to Run
**Step 1:** Make sure you have **Python 3.0+** installed.

**Step 2:** Install the project dependencies by running:
```bash
pip install -r requirements.txt
```

**Step 3: Update the database password** in `db/connection.py` to match your local PostgreSQL setup.

**Step 4:** Navigate to the project directory and run the linter:
```bash
python pylint .
```


Optional further steps:

**Step 5:** To run the Flask web app, execute:
```bash
python app.py
```

**Step 6:** Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the website.