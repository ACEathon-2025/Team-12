import sqlite3

conn = sqlite3.connect('database/faces.db')
c = conn.cursor()

# Add a test log entry
c.execute('INSERT INTO visit_logs (name, action) VALUES (?, ?)', ('TestUser', 'TestAction'))
conn.commit()
conn.close()
print("Test log added!")
