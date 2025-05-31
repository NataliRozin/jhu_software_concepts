from scrape import GradCafeScraper
from clean import clean_data, save_data

scraper  = GradCafeScraper()
raw_rows = scraper.scrape_data([1, 2])
structured_data = clean_data(raw_rows, scraper.base_url)
save_data(structured_data)