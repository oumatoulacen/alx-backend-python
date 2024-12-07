#!/usr/bin/env python3
'''create a generator that streams rows from an SQL database one by one.'''

import mysql.connector

config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'ALX_prodev'
    }

def stream_users():
    '''stream rows from an SQL database one by one.'''
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")
    for row in cursor:
        yield row
    cursor.close()
    connection.close()