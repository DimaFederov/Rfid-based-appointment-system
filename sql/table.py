import sqlite3

# Step 1: Connect to the local SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('local_attendance.db')

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Create the attendance table
cursor.execute('''
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    rfid_tag TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    reason TEXT
)
''')

# Step 4: Commit the changes
conn.commit()

# Step 5: Close the connection
conn.close()

print("Local database and table created successfully!")
