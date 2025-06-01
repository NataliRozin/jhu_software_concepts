# Name
NataliRozin (JHED ID: nrozin1)

# Module Info
**Module 2:** Web Scraping

**Assignment:** GradCafe Admissions Scraper  

**Due Date:** 01/06/2025

# Approach
This project implements a web scraper that extracts and structures graduate admissions data from [The GradCafe](https://www.thegradcafe.com), a site where applicants share admission outcomes of their graduate school. The project demonstrate cores skills in:
- URL management using `urllib3`
- HTML parsing with `BeautifulSoup`
- Data extraction using regex and string methods
- Data cleaning
- JSON formatting and storage

The approach was divided into three main components:

1. Scraping (`scrape.py`):
   - The `GradCafeScraper` class manages data collection.
   - It verifies permission to scrape using the `/robots.txt` file via `robotparser`.
   - Data is requested page-by-page using `urllib3.PoolManager`.
   - HTML content is parsed using `BeautifulSoup`, collecting all `<tr>` table rows from the survey pages.

2. Cleaning (`clean.py`):
   - The `clean_data()` function processes raw rows and extracts structured information.
   - Entries are identified by unique URLs and contain university, program name, degree (if available), application status, publish date, and a direct URL.
   - A second parsing step processes additional information from single-column rows (e.g., term, GPA, GRE scores, and comments).
   - The `clean_html()` function strips unwanted line breaks and special formatting such as `/"word/"`, converting it to `'word'`.
   - Data is stored consistently, ensuring missing values are either omitted or left as `None`.

3. Saving and Optional Loading (`main.py`):
   - The `save_data()` function saves the output as a formatted JSON file (`gradcafe_data.json`) using `json.dump()`.
   - A `load_data()` function was also included to load the file if needed, although it is not currently used in the main flow.

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