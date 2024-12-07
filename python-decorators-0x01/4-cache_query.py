#!/usr/bin/env python3
''' cache query results '''

import time
import sqlite3 
import functools

query_cache = {}

# with_db_connection = __import__('1-with_db_connection').with_db_connection
def with_db_connection(func):
    """ decorator to open and close database connections """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        result = func(conn, *args, **kwargs)
        conn.close()
        return result
    return wrapper

def cache_query(func):
    ''' decorator to cache query results '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        if query in query_cache:
            print(f'cache hit for {query}')
            return query_cache[query]
        print(f'cache miss for {query}')
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
start = time.time()
users = fetch_users_with_cache(query="SELECT * FROM users")
end = time.time()
print('First call took', end - start)

#### Second call will use the cached result
start = time.time()
users_again = fetch_users_with_cache(query="SELECT * FROM users")
end = time.time()
print('Second call took', end - start)