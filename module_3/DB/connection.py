import psycopg

def get_db_connection():
    DB_CONFIG = {
        "host":     "localhost",
        "dbname":   "gradCafe",
        "user":     "postgres",
        "password": "N@t@!ush2395P@sah!tz@",
        "port":     5432
    }
    
    try:
        # Create a connection to the PostgreSQL database
        return psycopg.connect(**DB_CONFIG)
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None