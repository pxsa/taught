# DataBase

## Table of Contents

- [SQLite](#sqlite)
- [MySQL](#mysql)

## SQLite

`SQLite` is probably the most straightforward database to connect since you don't need to install any external Python SQL modules to do so.

In addition, SQLite doesn't need server, because they interact with files.

```python
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None

    try:
        connection = sqlite3.connect(path)
        print("Connect successfully!")
    except Error as e:
        print(f"The error `{e}` occurred")

    return connection


connection = create_conntion("some/path")

```

## MySQL

There isn't any default Python SQL module that can use to connect to a MySQL database. so you need to install a Python SQL driver for MySQL in order to interact with a `MySQL` database.

### Download

> $ pip install mysql_connector-python

Note that `MySQL` is a server-based database management system. MySQL database has a two-step connection:

1. **Make a connection** to `MySQL` server.
2. **Execute a separate query** to create the database.

``` python
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("Connected successfully!")
    except Error as e:
        print(f"The error {e} occurred")
    
    return connection

connection = create_connection("localhost", "root", "", "test")

```

so far we've only established the connection. The database is not yet created. To do this, we need to define another function which needs a connection object to the database server that we want to interat with and secondly we need a `query` to create the databse.

``` python
def create_database(connection , query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        print("Database created successfully!")
    except Error as e:
        print(f"The error {e} occurred")

query = "CREATE DATABASE test"
create_Database(connection, query)

```
