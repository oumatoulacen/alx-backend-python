#!/usr/bin/env python3
'''Simulte fetching paginated data from the users database using a generator to lazily load each page'''

import mysql.connector

seed = __import__('seed')
config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'ALX_prodev'
    }

def paginate_users(page_size, offset):
    '''paginate users in the database'''
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s;", (page_size, offset))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def lazy_paginate(page_size):
    '''lazily paginate users in the database'''
    offset = 0
    while True:
        rows = paginate_users(page_size, offset)
        offset += page_size
        if not rows:
            break
        yield rows
    return None