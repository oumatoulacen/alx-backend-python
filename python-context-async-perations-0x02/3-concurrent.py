#!/usr/bin/env python3
''' Run multiple database queries concurrently using asyncio.gather '''

import asyncio
import aiosqlite

async def async_fetch_users():
    ''' fetch users from database '''
    async with aiosqlite.connect('users.db') as connection:
        cursor = await connection.execute('SELECT * FROM users')
        return await cursor.fetchall()

async def async_fetch_older_users():
    ''' fetch older users from database '''
    async with aiosqlite.connect('users.db') as connection:
        cursor = await connection.execute('SELECT * FROM users WHERE age > 40')        
        return await cursor.fetchall()

async def fetch_concurrently():
    ''' fetch users concurrently '''
    users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return users, older_users

if __name__ == '__main__':
    USERS, OLDER_USERS = asyncio.run(fetch_concurrently())
    print('Users:')
    for user in USERS:
        print(user)
    print('Older Users:')
    for user in OLDER_USERS:
        print(user)