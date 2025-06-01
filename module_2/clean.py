import re
import json

def contains_digit(text):
    """Check if the input text contains any digit."""
     # Use regex search to detect any digit in the string
    return bool(re.search(r'\d', text))

def clean_html(text):
    """ 
    Clean up HTML-like formatting and whitespace in the input text.

    Specifically:
    - Replace patterns like /"word/" with 'word'
    - Flatten line breaks and normalize whitespace
    """

    # Replace /"word/" pattern with 'word'
    text = re.sub(r'/\"(.*?)\"/', r"'\1'", text)

    # Replace line breaks (with optional surrounding whitespace) by a single space to flatten lines
    text = re.sub(r'\s*\r?\n\s*', ' ', text)

    # Collapse multiple consecutive spaces into a single space
    text = re.sub(r'\s+', ' ', text)

    # Remove leading/trailing whitespace
    return text.strip()

def parse_single_column(column_data, applicant):
    """
    Parse a single-column HTML content to extract additional applicant information,
    
     Returns updated applicant dictionary.
    """
    updates = {}
    
    # Extract term like 'Fall 2024' or 'Spring 2023'
    term = re.search(r'\b(Fall\s+\d{4}|Spring\s+\d{4})\b', column_data, flags=re.IGNORECASE)
    if term:
        updates["term"] = term.group(1)

    # Extract applicant origin (either 'international' or 'american')
    us_intl = re.search(r'\b(international|american)\b', column_data, flags=re.IGNORECASE)
    if us_intl:
        updates["applicant_origin"] = us_intl.group(1)

    # Extract GPA value (format: 'GPA 3.75')
    gpa = re.search(r'\bGPA\s+(\d\.\d{1,2})', column_data, re.IGNORECASE)
    if gpa:
        updates["GPA"] = gpa.group(1)
    
    # Extract GRE total score (format: 'GRE 320')
    gre = re.search(r'\bGRE\s+(\d+)', column_data, re.IGNORECASE)
    if gre:
        updates["GRE"] = gre.group(1)

    # Extract GRE verbal score (format: 'GRE V 160')
    gre_v = re.search(r'\bGRE\s+V\s+(\d+)', column_data, re.IGNORECASE)
    if gre_v:
        updates["GRE_V"] = gre_v.group(1)

    # Extract GRE analytical writing score (format: 'GRE AW 4')
    gre_aw = re.search(r'\bGRE\s+AW\s+(\d+)', column_data, re.IGNORECASE)
    if gre_aw:
        updates["GRE_AW"] = gre_aw.group(1)

    # Extract any comments wrapped in <p> HTML tags, then clean the comment text
    comment = re.search(r'<p[^>]*>(.*?)</p>', column_data, flags=re.DOTALL | re.IGNORECASE)
    if comment:
        updates["comment"] = clean_html(comment.group(1))
    
    # Update the applicant dictionary with all found information
    applicant.update(updates)
    return applicant

def clean_data(rows, base_url):
    """
    Parse rows of HTML table data and extract structured information into a dictionary.

    Each entry may span multiple rows, so entry identification persists across iterations.
    """

    # Create a dictionary to store data
    applicants_data = {}
    entry_num       = None # Tracks current applicant entry being parsed

    # Scrape data
    for row in rows:
        # Store columns data
        cols = row.find_all("td")
        
        # Attempt to detect new entry and extract entry_num
        match = re.findall(r'/result/\d+', str(row))
        if match:
            entry     = match[0]
            entry_num = entry.replace("/result/", "")

        if len(cols) >= 4:
            university = cols[0].text.strip()

            # Skip entries with invalid university names
            if contains_digit(university):
                entry_num = None
                continue
            
            # Split program info, where first part is program name, second is degree
            full_program = cols[1].text.strip().split('\n\n\n\n')

            # Build dictionary for this entry
            data = {"university": cols[0].text.strip(),
                    "program": full_program[0],
                    "publish_date": cols[2].text.strip(),
                    "url": base_url + entry,
                    "status": cols[3].text.strip(),
                                                    }
            if len(full_program) > 1:
                data["degree"] = full_program[1]

            # Store this applicant's data keyed by entry_num
            applicants_data[entry_num] = data
                          
        elif (len(cols) == 1) and entry_num:
            # Parse additional info in single column rows
            parse_single_column(str(cols), applicants_data[entry_num])

    return applicants_data

def save_data(data, filename='applicant_data.json'):
    """Save parsed data as a formatted JSON file."""

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"{len(data)} entries were saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data(filename='applicant_data.json'):
    """Load parsed data from a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None