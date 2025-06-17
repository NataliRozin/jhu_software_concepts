"""
query_data.py
=============

This module defines the `Query` class, which encapsulates common SQL queries
executed against the `applicants` PostgreSQL database.

Classes
-------
:class:`Query`
    A class that provides methods for executing predefined queries such as
    counting entries, calculating averages, and retrieving specific applicant statistics.

Typical usage example::

    q = Query()
    count = q.count_fall25_entries()
"""

from psycopg import Error, sql
from db.connection import get_db_connection

class Query:
    """
    A class to execute predefined SQL queries on the applicants database.

    :ivar connection: A psycopg database connection object.
    :vartype connection: psycopg.Connection
    """

    def __init__(self):
        """
        Initializes the Query object by establishing a database connection.
        """
        self.connection = get_db_connection()

    def count_fall25_entries(self) -> int:
        """
        Count how many entries in the database are for applicants who applied for Fall 2025.

        :return: The number of applicants who applied for Fall 2025.
        :rtype: int
        """

        # Compose SQL query using safe SQL construction
        select_stmt = sql.SQL("""
                    SELECT COUNT({field}) FROM {table_name}
                    WHERE {field} = %s
                    LIMIT {limit}
                """).format(
                    field = sql.Identifier('term'),
                    table_name = sql.Identifier('applicants'),
                    limit = sql.Literal(1)
            )

        params = ('Fall 2025',)

        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(select_stmt, params)
                result = cur.fetchone()
                return result[0]

        except Error as e:
            print(f"Database error executing {self.count_fall25_entries.__name__}: {e}")
            return 0

    def international_percentage(self) -> float:
        """
        Calculate the percentage of applicants who are international students,
        excluding those categorized as American or Other.

        :return: Percentage of international applicants rounded to two decimals.
        :rtype: float
        """
        select_stmt = sql.SQL("""
                    SELECT ROUND(
                        100.0 * COUNT({field})
                        FILTER (WHERE {field} = %s) / COUNT(*), 2
                    )
                    FROM {table_name}
                    LIMIT {limit}
                """).format(
                    field = sql.Identifier('us_or_international'),
                    table_name = sql.Identifier('applicants'),
                    limit = sql.Literal(1)
                )

        params = ('International',)

        try:
            with self.connection.cursor() as cur:
                cur.execute(select_stmt, params)
                result = cur.fetchone()
                return result[0] if result else 0.0

        except Error as e:
            print(f"Database error executing {self.international_percentage.__name__}: {e}")
            return 0.0

    def average_scores_international_fall25(self) -> list[float]:
        """
        Calculate the average GPA, GRE, GRE V, and GRE AW scores
        for international applicants who applied for Fall 2025,
        including valid ranges and rounding to two decimal places.

        :return: A list containing the averages [GPA, GRE, GRE_V, GRE_AW].
        :rtype: list[float]
        """

        select_stmt = sql.SQL("""
                        SELECT AVG({field_1}), AVG({field_2}), AVG({field_3}), AVG({field_4})
                        FROM {table_name}
                        WHERE {field_5} = %s
                            AND {field_6} = %s
                            AND {field_1} BETWEEN 0 AND 4.0
                            AND {field_2} BETWEEN 260 AND 340
                            AND {field_3} BETWEEN 130 AND 170
                            AND {field_4} BETWEEN 0 AND 6
                            AND MOD(({field_4} * 10)::INT, 5) = 0
                        LIMIT {limit}
                """).format(
                    field_1 = sql.Identifier('gpa'),
                    field_2 = sql.Identifier('gre'),
                    field_3 = sql.Identifier('gre_v'),
                    field_4 = sql.Identifier('gre_aw'),
                    field_5 = sql.Identifier('term'),
                    field_6 = sql.Identifier('us_or_international'),
                    table_name = sql.Identifier('applicants'),
                    limit = sql.Literal(1)
                )

        params = ("Fall 2025", "International")

        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(select_stmt, params)
                result = cur.fetchall()

                # Extract the tuple, round each element to 2 decimals, and return as list
                rounded_list = [round(x, 2) for x in result[0]] if result else [0.0, 0.0, 0.0, 0.0]

                return rounded_list

        except Error as e:
            print(
                f"Database error executing {self.average_scores_international_fall25.__name__}: {e}"
            )
            return [0.0, 0.0, 0.0, 0.0]

    def average_gpa_american_fall25(self) -> float:
        """
        Calculate the average GPA of American applicants who applied for Fall 2025
        with valid GPA scores.

        :return: The average GPA rounded to two decimals.
        :rtype: float
        """

        select_stmt = sql.SQL("""
                    SELECT AVG({field_1}) FROM {table_name}
                    WHERE {field_2} = %s
                    AND {field_3} = %s
                    AND {field_1} BETWEEN 0 AND 4.0
                    LIMIT {limit}
                """).format(
                    field_1 = sql.Identifier('gpa'),
                    field_2 = sql.Identifier('term'),
                    field_3 = sql.Identifier('us_or_international'),
                    table_name = sql.Identifier('applicants'),
                    limit = sql.Literal(1)
                )

        params = ("Fall 2025", "American")

        try:
            # Open cursor to perform database operations
            with self.connection.cursor() as cur:
                cur.execute(select_stmt, params)
                result = cur.fetchone()
                return round(result[0], 2)

        except Error as e:
            print(f"Database error executing {self.average_gpa_american_fall25.__name__}: {e}")
            return 0.0

    def accepted_fall25_percentage(self) -> float:
        """
        Calculate the percentage of accepted applicants among those who applied for Fall 2025.

        :return: The acceptance percentage rounded to two decimals.
        :rtype: float
        """
        select_stmt = sql.SQL("""
                    SELECT ROUND(
                        100.0 * COUNT({field_1})
                        FILTER (WHERE {field_1} LIKE %s AND {field_2} = %s) / COUNT(*), 2)
                    FROM {table_name}
                    LIMIT {limit}
                """).format(
                    field_1 = sql.Identifier('status'),
                    field_2 = sql.Identifier('term'),
                    table_name = sql.Identifier('applicants'),
                    limit = sql.Literal(1)
                )

        params = ('%Accepted%', 'Fall 2025')

        try:
            with self.connection.cursor() as cur:
                cur.execute(select_stmt, params)
                result = cur.fetchone()
                return result[0] if result and result[0] is not None else 0.0

        except Error as e:
            print(f"Database error executing {self.accepted_fall25_percentage.__name__}: {e}")
            return 0.0

    def average_gpa_accepted_fall25(self) -> float:
        """
        Calculate the average GPA of applicants accepted for Fall 2025
        with valid GPA scores.

        :return: The average GPA rounded to two decimals.
        :rtype: float
        """
        select_stmt = sql.SQL("""
                    SELECT AVG({field_1}) FROM {table_name}
                    WHERE {field_2} = %s
                    AND {field_3} LIKE %s
                    AND {field_1} BETWEEN 0 AND 4.0
                    LIMIT {limit}
                """).format(
                    field_1 = sql.Identifier('gpa'),
                    field_2 = sql.Identifier('term'),
                    field_3 = sql.Identifier('status'),
                    table_name = sql.Identifier('applicants'),
                    limit = sql.Literal(1)
                )

        params = ("Fall 2025", "%Accepted%")

        try:
            with self.connection.cursor() as cur:
                cur.execute(select_stmt, params)
                result = cur.fetchone()
                return round(result[0], 2) if result and result[0] is not None else 0.0

        except Error as e:
            print(f"Database error executing {self.average_gpa_accepted_fall25.__name__}: {e}")
            return 0.0

    def count_jhu_cs_masters(self) -> int:
        """
        Count the number of applicants who applied to Johns Hopkins University
        for a Master's degree in Computer Science.

        :return: The number of such applicants.
        :rtype: int
        """
        select_stmt = sql.SQL("""
                    SELECT COUNT(*) FROM {table_name}
                    WHERE ({field_1} LIKE %s OR LOWER({field_1}) LIKE %s)
                    AND ({field_1} LIKE %s OR LOWER({field_1}) LIKE %s)
                    AND {field_2} = %s
                    LIMIT {limit}
                """).format(
                    field_1 = sql.Identifier('program'),
                    field_2 = sql.Identifier('degree'),
                    table_name = sql.Identifier('applicants'),
                    limit = sql.Literal(1)
                )

        params = ('%JHU%', '%johns hopkins%', '%CS%', '%computer science%', 'Masters')

        try:
            with self.connection.cursor() as cur:
                cur.execute(select_stmt, params)
                result = cur.fetchone()
                return result[0] if result and result[0] is not None else 0

        except Error as e:
            print(f"Database error executing {self.count_jhu_cs_masters.__name__}: {e}")
            return 0
