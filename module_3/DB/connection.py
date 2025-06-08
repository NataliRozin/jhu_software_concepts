import psycopg

def get_db_connection():
    """
    Connects to the PostgreSQL database with preset parameters.

    Returns:
        psycopg.Connection
    """
    
    # PostgreSQL connection settings
    DB_CONFIG = {
        "host":     "localhost",
        "dbname":   "gradCafe",
        "user":     "postgres",
        "password": "Password",
        "port":     5432
    }
    
    try:
        # Create a connection to the PostgreSQL database
        return psycopg.connect(**DB_CONFIG)
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None