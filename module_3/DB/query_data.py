import psycopg
from psycopg import OperationalError
from load_data import DataLoader

class Query:
    def __init__(self, db_config):
        # Initialize with database configuration and path to JSON data
        self.db_config  = db_config

        # Create a connection to the PostgreSQL database
        self.connection = psycopg.connect(**self.db_config)
    
    def count_fall25_entries(self):
        # How many entries do you have in your database who have applied for Fall 2025?
        query = """
                SELECT COUNT(term) FROM applicants
                WHERE term = 'Fall 2025';
                """
        
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
                return result[0]
            
        except Exception as e:
            print(f"Error executing query: {e}")
    
    def international_percentage(self):
        # What percentage of entries are from international students (not American or Other) (to two decimal places)?
        query = """
                SELECT ROUND(
                 100.0 * COUNT(us_or_international)
                 FILTER (WHERE us_or_international = 'International') / COUNT(*), 2) AS international_percentage
                FROM applicants;
                """
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
                return result[0]
            
        except Exception as e:
            print(f"Error executing query: {e}")
    
    def average_scores_international_fall25(self):
        # What is the average GPA, GRE, GRE V, GRE AW of applicants who provide these metrics?
        query = """
                SELECT AVG(GPA), AVG(GRE), AVG(GRE_V), AVG(GRE_AW)
                FROM applicants
                WHERE term = 'Fall 2025'
                AND us_or_international = 'International';
                """
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
                return result[0]
            
        except Exception as e:
            print(f"Error executing query: {e}")

    def average_gpa_american_fall25(self):
        # What is their average GPA of American students in Fall 2025?
        query = """
                SELECT AVG(GPA) FROM applicants
                WHERE term = 'Fall 2025'
                AND us_or_international = 'American';
                """
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
                return result[0]
            
        except Exception as e:
            print(f"Error executing query: {e}")

    def count_accepted_fall25(self):
        # What percent of entries for Fall 2025 are Acceptances (to two decimal places)?
        query = """
                SELECT COUNT(status) FROM applicants
                WHERE term = 'Fall 2025'
                AND status = status LIKE '%Accepted%';
                """
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
                return result[0]
            
        except Exception as e:
            print(f"Error executing query: {e}")
        
    def avg_gpa_accepted_fall25(self):
        # What is the average GPA of applicants who applied for Fall 2025 who are Acceptances?
        query = """
                SELECT AVG(GPA) FROM applicants
                WHERE term = 'Fall 2025'
                AND status = status LIKE '%Accepted%';
                """
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
                return result[0]
            
        except Exception as e:
            print(f"Error executing query: {e}")
        
    def count_jhu_cs_masters(self):
        # How many entries are from applicants who applied to JHU for a masters degrees in Computer Science?
        query = """
                SELECT COUNT(*) FROM applicants
                WHERE (program LIKE '%JHU%' OR LOWER(program) LIKE '%johns hopkins%')
                AND (program LIKE '%CS%' OR LOWER(program) LIKE '%computer science%')
                AND degree = 'Masters';
                """
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
                return result[0]
            
        except Exception as e:
            print(f"Error executing query: {e}")