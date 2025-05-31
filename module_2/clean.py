import urllib3
from bs4 import BeautifulSoup
import re
import json

def clean_data(rows, base_url):
    # Create a dictionary to store data
    info = dict()

    # Scrape data
    for row in rows:
        # Store columns data
        cols = row.find_all("td")

        match = re.findall(r'/result/\d+', str(row))
        if match:
            entry     = match[0]
            entry_num = entry.replace("/result/", "")

        if len(cols) >= 4:
            full_program = cols[1].text.strip().split('\n\n\n\n')

            info[entry_num] = {"program": f"{cols[0].text.strip()}, {full_program[0]}",
                                                      "publish date": cols[2].text.strip(),
                                                      "url": base_url + entry,
                                                      "status": cols[3].text.strip(),
                                                      "term": "",
                                                      "degree": full_program[1]
                                                      }
        elif len(cols) == 1:
            term = re.findall(r'\b(Fall\s+\d{4}|Spring\s+\d{4})\b', str(cols), flags=re.IGNORECASE)
            if term:
                info[entry_num].update({"term": term[0]})

            us_intl = re.findall(r'\b(international|american)\b', str(cols), flags=re.IGNORECASE)
            if us_intl:
                info[entry_num].update({"applicant origin": us_intl[0]})

            gpa = re.findall(r'\bGPA\s+\d\.\d{1,2}', str(cols), re.IGNORECASE)
            if gpa:
                info[entry_num].update({"GPA": gpa[0].upper().replace("GPA", "").strip()})
            
            gre = re.findall(r'\bGRE\s+\d+', str(cols), re.IGNORECASE)
            if gre:
                info[entry_num].update({"GRE": gre[0].upper().replace("GRE", "").strip()})

            gre_v = re.findall(r'\bGRE\s+V\s+\d+', str(cols), re.IGNORECASE)
            if gre_v:
                info[entry_num].update({"GRE V": re.sub(r'[^\d]', '', gre_v[0])})

            gre_aw = re.findall(r'\bGRE\s+AW\s+\d+', str(cols), re.IGNORECASE)
            if gre_aw:
                info[entry_num].update({"GRE AW": re.sub(r'[^\d]', '', gre_aw[0])})

            comment = re.search(r'<p[^>]*>(.*?)</p>', str(cols), flags=re.DOTALL | re.IGNORECASE)
            if comment:
                info[entry_num].update({"comment": comment.group(1)})

    return info

def save_data(data, filename='gradcafe_data.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)