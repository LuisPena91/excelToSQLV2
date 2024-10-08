import mysql.connector
import json
import os
from menu import menu2

#db credentials
def credentials():
    while True:
        sql_database = load_sql_database()
        if sql_database is None:
            print('Input the data base information: ')
            host = str(input("host: "))
            user = str(input("user: "))
            password = str(input("password: "))
            name = str(input("Data base name: "))
            sql_database = []
            sql_database.append(host)
            sql_database.append(user)
            sql_database.append(password)
            sql_database.append(name)
            save_sql_database(sql_database)
            try:
                connect_to_database()
                break
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                #delete_sql_database()
    return sql_database
#Conect to db
def connect_to_database():
    sql_database = load_sql_database()
    if sql_database is None:
        sql_database = credentials()
    return mysql.connector.connect(
        host = sql_database[0],
        user = sql_database[1],
        password = sql_database[2],
        database = sql_database[3]
    )
#func to look for the tables who belong to the DB
def table_name_sql(database_name):
    try:
        connection = connect_to_database()
    except mysql.connector.Error as err:
        print('CONNECTION ERROR')
        print(f"Error: {err}")  
    cursor = connection.cursor()
    cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{database_name}'")
    tables_names = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return tables_names
#func to select a table to update
def table_selection(database_name):
    print("----Data base Tables----") 
    tables_name = table_name_sql(database_name)
    for j in range(len(tables_name)):
        print(f" - {j+1}:  {tables_name[j][0]}")
    print(" - 0:  Return")
    pos_sql = menu2(j+1)
    return pos_sql -1
#func to look for the columns who belong to the table selected
def column_name_sql(table_selected):
    try:
        connection = connect_to_database()
    except mysql.connector.Error as err:
        print('CONNECTION ERROR')
        print(f"Error: {err}")
    cursor = connection.cursor()
    cursor.execute(f"""SHOW COLUMNS FROM {table_selected};""")
    column_names = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return column_names
#func to select a column to update
def column_selection(sql_database,table_selected):
    print(f"Columns in the SQL table {table_selected}: ")
    for j in range(len(column_name_sql(sql_database,table_selected))):
        print(f"{j+1}:  {column_name_sql(sql_database,table_selected)[j][0]}")
    pos_column = int(input(f'Select a SQL column from {table_selected} to update: '))
    return pos_column-1

file_sql_database = 'sql_database.json'
#Func to load sql info
def load_sql_database():
    if os.path.exists(file_sql_database):
        with open(file_sql_database, 'r') as file:
            return json.load(file)
        return None

#Func to save SQl info
def save_sql_database(sql_database):
    with open(file_sql_database, 'w') as file:
        json.dump(sql_database, file)

#Func to clean the SQL info
def delete_sql_database():
    if os.path.exists(file_sql_database):
        os.remove(file_sql_database)