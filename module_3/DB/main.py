from pathlib import Path
from load_data import DataLoader
from query_data import Query

# Main execution block
if __name__ == "__main__":
    # Define the PostgreSQL connection configuration
    db_config = {
        "host":     "localhost",
        "dbname":   "gradCafe",
        "user":     "postgres",
        "password": "N@t@!ush2395P@sah!tz@",
        "port":     5432
    }
    
    # Full path to the JSON data file
    json_path = 'applicant_data.json'

    # Instantiate the DataLoader class
    loader = DataLoader(db_config, json_path)

    # Load applicant data from the JSON file
    applicants_info = loader.load_data()

    # Create the applicants table in the database
    loader.create_table(applicants_info)

    # Execute queries
    queriesExecuter = Query(db_config)
    num = queriesExecuter.count_fall25_entries()