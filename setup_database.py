import sqlite3

conn = sqlite3.connect('database/faces.db')
c = conn.cursor()

# Table for known faces
c.execute('''
CREATE TABLE IF NOT EXISTS known_faces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    embedding BLOB NOT NULL
)
''')

# Table for visit logs
c.execute('''
CREATE TABLE IF NOT EXISTS visit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    action TEXT
)
''')

conn.commit()
conn.close()
