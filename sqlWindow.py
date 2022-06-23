import sqlite3
while True:
    try:
        sqlite3Command = input("sqlite3>")
        if '.open' in sqlite3Command:
            fileName = sqlite3Command.replace(".open ", "")
            connection = sqlite3.connect(fileName)
            cursor = connection.cursor()
        elif sqlite3Command == 'quit':
            quit()
        else:
            cursor.execute(sqlite3Command)
            records = cursor.fetchall()
            for record in records:
                print(record)
            connection.commit()
    except Exception as e:
        print(e)



# import pyodbc
# # Trusted Connection to Named Instance
# connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQL2K19;DATABASE=SampleDB;Trusted_Connection=yes;')
# cursor=connection.cursor()
# cursor.execute("SELECT @@VERSION as version")
# while 1:
#     row = cursor.fetchone()
#     if not row:
#         break
#     print(row.version)
# cursor.close()
# connection.close()



# import mysql.connector
# from mysql.connector import Error
# import pandas as pd
# import pyodbc
# def create_db_connection(host_name, user_name, user_password, db_name):
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host=host_name,
#             user=user_name,
#             passwd=user_password,
#             database=db_name
#         )
#         print("MySQL Database connection successful")
#     except Error as err:
#         print(f"Error: '{err}'")

#     return connection

# create_db_connection('localhost', 'root', pow, db)