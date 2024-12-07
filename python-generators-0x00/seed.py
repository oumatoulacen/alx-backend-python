#!/usr/bin/env python3
'''create a generator that streams rows from an SQL database one by one.'''

import mysql.connector
from uuid import uuid4 as uuid

config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'ALX_prodev'
    }

def connect_db():
    '''connect to the database'''
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        )
    return connection

def connect_to_prodev():
    '''connect to the database'''
    connection = mysql.connector.connect(**config)
    return connection

def create_database(connection):
    '''create a database'''
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    cursor.close()

def create_table(connection):
    '''create a table'''
    cursor = connection.cursor()
    stmt = '''CREATE TABLE IF NOT EXISTS user_data (
        id CHAR(36) PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        age DECIMAL NOT NULL
        );
        CREATE INDEX user_data_id ON user_data (id);
        '''
    cursor.execute(stmt)

def insert_data(connection, filename):
    '''insert data into the table'''
    if not connection.is_connected():
        '''reconnect if connection is closed'''
        connection.reconnect()
    cursor = connection.cursor()
    stmt = '''INSERT INTO user_data (id, name, email, age) VALUES (uuid(), %s, %s, %s);'''
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            row = line.strip().split(',')
            cursor.execute(stmt, (row[0], row[1], int(row[2][1:-1])))
    connection.commit()
    cursor.close()

