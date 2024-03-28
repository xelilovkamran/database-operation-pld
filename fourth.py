import mysql.connector
import random
import string


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="library"
)
cursor = conn.cursor()

# Create the tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Authors (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255),
                    author_id INT,
                    FOREIGN KEY (author_id) REFERENCES Authors(id))''')

cursor.execute(f"INSERT into authors (name) VALUES ('{randomword(8)}')")
author_id = cursor.lastrowid
cursor.execute(
    f"""INSERT INTO books (title, author_id) VALUES
    ('{randomword(10)}', {author_id}),
    ('{randomword(10)}', {author_id}),
    ('{randomword(10)}', {author_id})"""
)

conn.commit()
cursor.execute(
    f"SELECT title, name FROM Authors JOIN Books ON Authors.id = Books.author_id where books.author_id = {author_id}")

books = cursor.fetchall()

for book in books:
    print(book[0], "by", book[1])

# Commit changes and close connection
conn.close()
