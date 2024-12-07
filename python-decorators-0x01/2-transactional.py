#!/usr/bin/env python3
''' database transaction handling '''

import sqlite3
import functools
import traceback

def with_db_connection(func):
    """ decorator to open and close database connections """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = kwargs.get('conn')
        result = func(*args, **kwargs)
        conn.close()
        return result
    return wrapper

def transactional(func):
    ''' decorator to handle database transactions '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = kwargs.get('conn')
        try:
            result = func(*args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            traceback.print_exc()
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    ''' update user's email '''
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 

#### Update user's email with automatic transaction handling
conn = sqlite3.connect('users.db') 
update_user_email(conn=conn, user_id=1, new_email='Crawford_Cartwright@hotmail.com')