#!/usr/bin/env python3
''' class based context manager for database connection '''

import mysql.connector

class DatabaseConnection:
    ''' class to manage database connection '''
    def __init__(self, user, password, host, database):
        ''' constructor '''
        self.config = {
            'user': user,
            'password': password,
            'host': host,
            'database': database
        }

    def __enter__(self):
        ''' enter method '''
        self.connection = mysql.connector.connect(**self.config)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        ''' exit method '''
        self.connection.close()
        if exc_type is not None:
            return False
        return True


if __name__ == '__main__':
    with DatabaseConnection('root', 'root', 'localhost', 'ALX_prodev') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM user_data')
        for row in cursor.fetchall():
            print(row)
        cursor.close()
