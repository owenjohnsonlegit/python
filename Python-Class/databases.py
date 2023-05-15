import sqlite3

# Create a new SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a new table with field names and data types
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                    first_name TEXT,
                    last_name TEXT,
                    address TEXT,
                    city TEXT,
                    state TEXT,
                    zip TEXT,
                    phone_number TEXT
                )''')

# Insert four rows of data into the table
data = [
    ('John', 'Doe', '123 Main St', 'New York', 'NY', '10001', '555-1234'),
    ('Jane', 'Smith', '456 Elm St', 'San Francisco', 'CA', '94101', '555-5678'),
    ('Michael', 'Johnson', '789 Oak St', 'Chicago', 'IL', '60601', '555-9012'),
    ('Emily', 'Brown', '321 Pine St', 'Los Angeles', 'CA', '90001', '555-3456')
]

cursor.executemany('INSERT INTO contacts VALUES (?, ?, ?, ?, ?, ?, ?)', data)
conn.commit()

# Retrieve and display the data from the table
cursor.execute('SELECT * FROM contacts')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Delete a row from the table
cursor.execute('DELETE FROM contacts WHERE first_name = ?', ('Jane',))
conn.commit()

# Retrieve and display the data from the table again
cursor.execute('SELECT * FROM contacts')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the database connection
conn.close()

# Sources
# https://sqlite.org/datatype3.html

# Fake data
# https://www.mockaroo.com/
