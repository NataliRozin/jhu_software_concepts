import psycopg
from psycopg import OperationalError
from .connection import get_db_connection

class Query:
    """
    A class to execute predefined SQL queries on the applicants database.

    Attributes:
        connection: A psycopg database connection object.
    """

    def __init__(self):
        """
        Initializes the Query object by establishing a database connection.
        """
        self.connection = get_db_connection()
    
    def count_fall25_entries(self):
        """
        Counts how many entries in the database are for applicants who applied for Fall 2025.

        Returns:
            int: The number of applicants who applied for Fall 2025.
        """

        query = """
                SELECT COUNT(term) FROM applicants
                WHERE term = 'Fall 2025';
                """
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchone()
                return result[0]
            
        except Exception as e:
            print(f"Error executing query: {e}")
    
    def international_percentage(self):
        """
        Calculates the percentage of applicants who are international students,
        excluding those categorized as American or Other.

        Returns:
            float: Percentage of international applicants rounded to two decimals.
        """

        query = """
                SELECT ROUND(
                 100.0 * COUNT(us_or_international)
                 FILTER (WHERE us_or_international = 'International') / COUNT(*), 2)
                FROM applicants;
                """
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchone()
                return result[0]
            
        except Exception as e:
            print(f"Error executing query: {e}")
    
    def average_scores_international_fall25(self):
        """
        Calculates the average GPA, GRE, GRE V, and GRE AW scores
        for international applicants who applied for Fall 2025, including valid ranges
        and rounding to two decimal places.

        Returns:
            list[float]: A list containing the averages [GPA, GRE, GRE_V, GRE_AW].
        """

        query = """
                SELECT AVG(GPA), AVG(GRE), AVG(GRE_V), AVG(GRE_AW)
                FROM applicants
                WHERE term = 'Fall 2025'
                AND us_or_international = 'International'
                AND GPA BETWEEN 0 AND 4.0
                AND GRE BETWEEN 260 AND 340
                AND GRE_V BETWEEN 130 AND 170
                AND GRE_AW BETWEEN 0 AND 6
                AND MOD((GRE_AW * 10)::INT, 5) = 0;
                """
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()

                # Extract the tuple, round each element to 2 decimals, and return as list
                rounded_list = [round(x, 2) for x in result[0]]

                return rounded_list
            
        except Exception as e:
            print(f"Error executing query: {e}")

    def average_gpa_american_fall25(self):
        """
        Calculates the average GPA of American applicants who applied for Fall 2025
        with valid GPA scores.

        Returns:
            float: The average GPA rounded to two decimals.
        """
        
        query = """
                SELECT AVG(GPA) FROM applicants
                WHERE term = 'Fall 2025'
                AND us_or_international = 'American'
                AND GPA BETWEEN 0 AND 4.0;
                """
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchone()
                return round(result[0], 2)
            
        except Exception as e:
            print(f"Error executing query: {e}")

    def count_accepted_fall25(self):
        """
        Calculates the percentage of accepted applicants among those who applied for Fall 2025.

        Returns:
            float: The acceptance percentage rounded to two decimals.
        """
        
        query = """
                SELECT ROUND(
                 100.0 * COUNT(status)
                 FILTER (WHERE status LIKE '%Accepted%' AND term = 'Fall 2025') /
                 COUNT(*), 2)
                FROM applicants;
                """
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchone()
                return result[0]
            
        except Exception as e:
            print(f"Error executing query: {e}")
        
    def average_gpa_accepted_fall25(self):
        """
        Calculates the average GPA of applicants accepted for Fall 2025
        with valid GPA scores.

        Returns:
            float: The average GPA rounded to two decimals.
        """
        
        query = """
                SELECT AVG(GPA) FROM applicants
                WHERE term = 'Fall 2025'
                AND status LIKE '%Accepted%'
                AND GPA BETWEEN 0 AND 4.0;
                """
        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(query)
                result = cur.fetchone()
                return round(result[0],2)
            
        except Exception as e:
            print(f"Error executing query: {e}")
        
    def count_jhu_cs_masters(self):
        """
        Counts the number of applicants who applied to Johns Hopkins University
        for a Master's degree in Computer Science.

        Returns:
            int: The number of such applicants.
        """
        
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
                result = cur.fetchone()
                return result[0]
            
        except Exception as e:
            print(f"Error executing query: {e}")