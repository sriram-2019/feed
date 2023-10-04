import sqlite3

# Connect to or create an SQLite database
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Query to get column information for the 'students' table
sql = "PRAGMA table_info(students);"
cursor.execute(sql)

# Fetch and print the column names
columns = cursor.fetchall()
for column in columns:
    print(column[1])  # Column name is in the second position (index 1)

# Commit the changes and close the connection
conn.commit()
conn.close()
