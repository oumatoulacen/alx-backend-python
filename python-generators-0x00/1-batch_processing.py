#!/usr/bin/env python3
'''Create a generator to fetch and process data in batches from the users database'''

import mysql.connector

config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'ALX_prodev'
    }

def stream_users_in_batches(batch_size):
    '''stream users in batches'''
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")
    while True:
        rows = cursor.fetchmany(size=batch_size)
        if not rows:
            break
        yield rows
    cursor.close()
    connection.close()

def batch_processing(batch_size: int):
    '''processes each batch to filter users over the age of25'''
    for batch in stream_users_in_batches(batch_size):
        for row in batch:
            if row[3] > 25:
                print(row)
    print()