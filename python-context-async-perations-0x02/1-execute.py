#!/usr/bin/env python3
''' Reusable Query Context Manager '''

import mysql.connector

class ExecuteQuery:
    ''' reusable context manager that takes a query as input and executes it'''
    def __init__(self, query, age):
        ''' constructor '''
        self.connection = mysql.connector.connect(
            host='localhost',
            database='ALX_prodev',
            user='root',
            password='root'
        )
        self.query = query
        self.age = age
    
    def __enter__(self):
        ''' enter method '''
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, (self.age,))
        return self.cursor.fetchall()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        ''' exit method '''
        self.cursor.close()
        self.connection.close()
        if exc_type is not None:
            return False
        return True

if __name__ == '__main__':
    with ExecuteQuery('SELECT * FROM user_data WHERE age > %s', 25) as results:
        for row in results:
            print(row)