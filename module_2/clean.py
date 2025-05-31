import urllib3
from bs4 import BeautifulSoup
import re
import json

def contains_digit(text):
    """Check if the input text contains any digit."""
    return bool(re.search(r'\d', text))

def parse_single_column(column_data, applicant):
    """
    Parse a single-column HTML string to extract additional applicant information,
    updating the applicant dictionary in-place.
    """
    term = re.findall(r'\b(Fall\s+\d{4}|Spring\s+\d{4})\b', column_data, flags=re.IGNORECASE)
    if term:
        applicant.update({"term": term[0]})

    us_intl = re.findall(r'\b(international|american)\b', column_data, flags=re.IGNORECASE)
    if us_intl:
        applicant.update({"applicant origin": us_intl[0]})

    gpa = re.findall(r'\bGPA\s+\d\.\d{1,2}', column_data, re.IGNORECASE)
    if gpa:
        applicant.update({"GPA": gpa[0].upper().replace("GPA", "").strip()})
    
    gre = re.findall(r'\bGRE\s+\d+', column_data, re.IGNORECASE)
    if gre:
        applicant.update({"GRE": gre[0].upper().replace("GRE", "").strip()})

    gre_v = re.findall(r'\bGRE\s+V\s+\d+', column_data, re.IGNORECASE)
    if gre_v:
        applicant.update({"GRE V": re.sub(r'[^\d]', '', gre_v[0])})

    gre_aw = re.findall(r'\bGRE\s+AW\s+\d+', column_data, re.IGNORECASE)
    if gre_aw:
        applicant.update({"GRE AW": re.sub(r'[^\d]', '', gre_aw[0])})

    comment = re.search(r'<p[^>]*>(.*?)</p>', column_data, flags=re.DOTALL | re.IGNORECASE)
    if comment:
        applicant.update({"comment": comment.group(1)})
    
    return applicant

def clean_data(rows, base_url):
    """
    Parse rows of HTML table data and extract structured information into a dictionary.
    Each entry may span multiple rows, so entry identification persists across iterations.
    """

    # Create a dictionary to store data
    applicants_data = {}

    # Scrape data
    for row in rows:
        # Store columns data
        cols = row.find_all("td")
        
        # Detect new entry and extract entry_num
        match = re.findall(r'/result/\d+', str(row))
        if match:
            entry     = match[0]
            entry_num = entry.replace("/result/", "")

        if len(cols) >= 4:
            university = cols[0].text.strip()

            # Skip entries with invalid university names
            if contains_digit(university):
                entry_num = ""
                continue
            else:
                full_program = cols[1].text.strip().split('\n\n\n\n')

                applicants_data[entry_num] = {"program": f"{cols[0].text.strip()}, {full_program[0]}",
                                              "publish date": cols[2].text.strip(),
                                              "url": base_url + entry,
                                              "status": cols[3].text.strip(),
                                                        }
                if len(full_program) > 1:
                    applicants_data[entry_num].update({"degree": full_program[1]})
                          
        elif (len(cols) == 1) and entry_num:
            # Parse additional info in single column rows
            parse_single_column(str(cols), applicants_data[entry_num])

    return applicants_data

def save_data(data, filename='gradcafe_data.json'):
    """
    Save parsed data to a JSON file with pretty formatting.
    """

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"{len(data)} entries were saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")