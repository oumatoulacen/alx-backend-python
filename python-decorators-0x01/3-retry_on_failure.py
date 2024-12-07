#!/usr/bin/env python3
''' retry a function on failure '''

import time
import sqlite3 
import functools

def with_db_connection(func):
    """ decorator to open and close database connections """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = kwargs.get('conn')
        result = func(*args, **kwargs)
        conn.close()
        return result
    return wrapper

def retry_on_failure(retries=3, delay=1):
    """ decorator to retry a function on failure """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f'{func.__name__} failed. Retrying in {delay} seconds.')
                    time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure
conn = sqlite3.connect('users.db')
users = fetch_users_with_retry(conn=conn)
print(users)