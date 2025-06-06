import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="******",
    database="testdatabase"
    )


cursor = connection.cursor()

cursor.execute("""            
CREATE TABLE IF NOT EXISTS users (
               id INT AUTO_INCREMENT PRIMARY KEY,
               username VARCHAR(50),
               password VARCHAR(50)
)
""")
insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
users_data = [
    ('Billy', 'simon456'),
    ('Mandy', 'mnbvc'),
    ('GRIM', '0987654')
]


cursor.executemany(insert_query, users_data)

connection.commit()

print(f"{cursor.rowcount} records inserted successfully.")


cursor.close()
connection.close()