import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="******",
    database="testdatabase"
    )

cursor= connection.cursor()

user_input=input("Enter user ID: ")               #    "1 OR 1=1" is a classic SQL Injection attack

query = f"SELECT * FROM users WHERE id = {user_input};"  # unsafe query taken into database

cursor.execute(query)

try:
    # Enable multiple statements with multi=True
    for result in cursor.execute(query, multi=True):
        if result.with_rows:
            print(result.fetchall())  # Fetch and print results
except mysql.connector.Error as err:
    print(f"Error: {err}")

results = cursor.fetchall()

for row in results:
    print(row)                       
cursor.close()
connection.close()