from scrape import GradCafeScraper
from clean import clean_data, save_data, load_data

# Initialize the scraper object for GradCafe
scraper  = GradCafeScraper()

# Scrape raw data
raw_rows = scraper.scrape_data(10)

# Clean and structure the raw data
structured_data = clean_data(raw_rows, scraper.base_url)

# Save the cleaned and structured data to a file or database
save_data(structured_data)

# Load the cleaned and saved GradCafe data for further analysis or processing
gradcafe_data = load_data()