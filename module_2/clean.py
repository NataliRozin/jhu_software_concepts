import urllib3
from bs4 import BeautifulSoup
import re
import json
    
def remove_duplicates(seq):
    # This function removes dupliactes from a list
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

def clean_data(rows, base_url):
    # Create a dictionary to store data
    info = dict()

    # Scrape data
    for row in rows:
        # Store columns data
        cols = row.find_all("td")

        entry = re.findall(r'/result/\d+', str(row))

        if len(cols) >= 4:
            full_program = cols[1].text.strip().split('\n\n\n\n')

            info[entry[0].replace("/result/", "")] = {"program": f"{cols[0].text.strip()}, {full_program[0]}",
                                                      "publish date": cols[2].text.strip(),
                                                      "url": base_url + entry[0],
                                                      "status": cols[3].text.strip(),
                                                      "term": "",
                                                      "degree": full_program[1]
                                                      }
    return info

def save_data(data, filename='gradcafe_data.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)