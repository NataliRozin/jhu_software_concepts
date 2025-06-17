"""
connection.py
===========

This module provides functionality to establish a connection to a PostgreSQL
database using the `psycopg` library.

Functions:
    get_db_connection -- Connects to the PostgreSQL database and returns a connection object.
"""

import psycopg # type: ignore

def get_db_connection():
    """
    Establish a connection to the PostgreSQL database using preset configuration.

    :returns: A connection object to the PostgreSQL database, or None if the connection fails.
    :rtype: psycopg.Connection or None
    :raises psycopg.Error: If an error occurs while trying to connect.
    """

    # PostgreSQL connection settings
    db_config = {
        "host":     "localhost",
        "dbname":   "gradCafe",
        "user":     "postgres",
        "password": "N@t@!ush2395P@sah!tz@",
        "port":     5432
    }

    try:
        # Create a connection to the PostgreSQL database
        return psycopg.connect(**db_config)
    except psycopg.Error as e:
        print(f"Database connection failed: {e}")
        return None
