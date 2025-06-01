# Name
Natali Rozin (JHED ID: nrozin1)

# Module Info
**Module 2:** Web Scraping

**Assignment:** GradCafe Admissions Scraper  

**Due Date:** 01/06/2025

# Approach
This project implements a web scraper designed to extract, clean, and structure graduate admissions data from [The GradCafe](https://www.thegradcafe.com), a platform where applicants share publicly their graduate school admission outcomes.

The solution is structured into three core components — scraping, data cleaning, and data persistence — each encapsulated in dedicated modules to ensure easy maintainability and clarity.

1. Scraping (`scrape.py`):
   - The `GradCafeScraper` class manages all aspects of data collection from the GradCafe site.
   - Scraper initialization (`__init__`) sets base URL, target path, user agent string, and configures an HTTP connection pool for requests using urllib3.PoolManager.
   - Before any scraping begins, `_check_permissions()` fetches and parses the site’s robots.txt using Python’s robotparser to verify that crawling the target path is permitted for the specified user agent. If disallowed or network issues arise, it raises explicit exceptions, enforcing compliance with site policies.
   - After confirming permissions, the `scrape_data(self, page_num)` method handles the core data extraction process, looping through the requested number of survey pages (up to 10,000+ entries as per requirements). For each page, it requests HTML content, parses it with BeautifulSoup, and extracts all relevant table row (<tr>) elements containing applicant data. These rows are returned as raw HTML snippets for further processing.
   - The scraper handles network errors by relying on urllib3’s connection pooling and built-in exception handling, ensuring reliability during large-scale scraping.

2. Cleaning (`clean.py`):
   Responsible for converting the raw HTML rows into clean, structured data entries.

   - `clean_data(rows, base_url)`  
     This function takes the raw rows collected from scraping and the base URL to build full applicant data dictionaries. It identifies unique entries by parsing URLs embedded in the rows and extracts data fields such as university name, program, degree type, publish date, status, and the direct URL link. It also handles rows that contain extended information like term start, GRE scores, GPA, and comments, calling helper functions to parse these. Missing data fields are handled by either omitting them or assigning `None`.

   - `parse_single_column(column_data, applicant)`  
     Parses a single-column HTML snippet related to an applicant to extract detailed attributes such as admission term (e.g., Fall 2024), applicant origin (international or American), GPA, GRE scores (total, verbal, analytical writing), and any textual comments. It uses regex searches to find this data and updates the applicant dictionary accordingly.

   - `clean_html(text)`  
     Cleans messy HTML formatting within comment strings or other text fields. Specifically, it replaces unusual patterns like `/"word/"` with `'word'`, removes line breaks by flattening them into spaces, collapses multiple whitespace characters into a single space, and trims leading/trailing whitespace to produce clean, readable text.

   - `contains_digit(text)`  
     A utility function that determines whether the provided string contains any numeric characters. This function is primarily used to validate university names by filtering out entries that include digits, thereby ensuring only legitimate university names are processed.

3. Data Persistence (within `clean.py`)
   - `save_data(data, filename='gradcafe_data.json')`  
     Saves the cleaned and structured data dictionary to a JSON file with proper formatting and UTF-8 encoding. the function includes error handling to report any issues during the writing process.

   - `load_data(filename='gradcafe_data.json')`  
     Loads JSON data from the specified file back into a Python dictionary for later use or analysis.

   This approach ensures the scraper respects site rules, collects extensive applicant data over many pages, cleans and structures that data into usable form, and saves it for future processing or analysis.

# How to Run
**Step 1:** Make sure you have **Python 3.0+** installed.

**Step 2:** Install the project dependencies by running:
```bash
pip install -r requirements.txt
```

**Step 3:** Navigate to the project directory and execute:
```bash
python main.py
```

The scraper will retrieve 10,000+ entries, clean the raw HTML data, and save it to:
```bash
applicant_data.json
```