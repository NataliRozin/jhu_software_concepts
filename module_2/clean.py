import urllib3
from bs4 import BeautifulSoup
import re
import json
    
def remove_duplicates(seq):
    # This function removes dupliactes from a list
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

def clean_data(rows):
    # Create a dictionary to store data
    info = dict()

    # Create rmpty lists to store data
    entry_num, university, program, degree, publish_date, status = [], [], [], [], [], []

    # Store the entry_num number - a unique code
    entry_num.extend(remove_duplicates(re.findall(r'/result/\d+', str(rows))))

    # Scrape data
    for row in rows:
        # Store columns data
        cols = row.find_all("td")

        if len(cols) >= 4:
            full_program = cols[1].text.strip().split('\n\n\n\n')

            university.append(cols[0].text.strip())
            publish_date.append(cols[2].text.strip())
            status.append(cols[3].text.strip())

            full_program = cols[1].text.strip().split('\n\n\n\n')
            program.append(full_program[0])
            degree.append(full_program[1])

    return entry_num, university, program, degree, publish_date, status

def save_data(data, filename='gradcafe_data.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)