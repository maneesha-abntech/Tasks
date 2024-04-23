import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM books')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()


#FETCHING ONLY SPECIFIC COLUMNS
'''
import sqlite3

# Establish connection to the SQLite database
conn = sqlite3.connect('test.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute the SQL query to select specific columns
cursor.execute('SELECT title, author FROM books')

# Fetch all rows
rows = cursor.fetchall()

# Iterate over the rows and print the values of the selected columns
for row in rows:
    title, author = row  # Unpack the values from the row tuple
    print("Title: {}, Author: {}".format(title, author))

# Close the connection
conn.close()

'''