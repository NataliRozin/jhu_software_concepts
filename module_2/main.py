from scrape import GradCafeScraper
from clean import clean_data, save_data

# Initialize the scraper object for GradCafe
scraper  = GradCafeScraper()

# Scrape raw data
raw_rows = scraper.scrape_data([1, 2])

# Clean and structure the raw data
structured_data = clean_data(raw_rows, scraper.base_url)

# Save the cleaned and structured data to a file or database
save_data(structured_data)