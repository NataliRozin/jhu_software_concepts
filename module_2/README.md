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

   - The `clean_data(rows, base_url)` function receives the raw HTML rows from scraping and systematically converts them into clean, structured Python dictionaries keyed by unique entry IDs.

   - It identifies new entries by detecting unique result URLs embedded within the rows, extracting core information such as university name, program name, degree type (Masters or PhD), status, publish date, and constructs absolute URLs for direct reference.

   - To maintain data integrity, entries with invalid university names (containing digits) are filtered out using the `contains_digit(text)` utility function.

   - Additional applicant attributes including semester and year of program start, applicant origin (international/American), GRE scores (total, verbal, analytical writing), GPA, and user comments , are parsed from single-column rows using `parse_single_column(column_data, applicant)`. This function uses regex searches to reliably extract varied formats of academic data and updates the applicant dictionary accordingly.

   - The `clean_html(text)` utilifty function cleans messy HTML formatting within comment strings or other text fields. Specifically, it replaces unusual patterns like `/"word/"` with `'word'`, removes line breaks by flattening them into spaces, collapses multiple whitespace characters into a single space, and trims leading/trailing whitespace to produce clean, readable text.

3. Data Persistence (within `clean.py`)
   - `save_data(data, filename='applicant_data.json')`  
     Saves the cleaned and structured data dictionary to a JSON file with proper formatting and UTF-8 encoding. the function includes error handling to report any issues during the writing process.

   - `load_data(filename='applicant_data.json')`  
     Loads JSON data from the specified file back into a Python dictionary for later use or analysis.

   This approach ensures the scraper respects site rules, collects extensive applicant data over many pages, cleans and structures that data into usable form, and saves it for future processing or analysis.

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
python main.py
```

The scraper will retrieve 10,000+ entries, clean the raw HTML data, and save it to:
```bash
applicant_data.json
```