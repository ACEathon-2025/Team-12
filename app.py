from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def logs():
    conn = sqlite3.connect('database/faces.db')
    c = conn.cursor()
    c.execute('SELECT name, timestamp, action FROM visit_logs ORDER BY timestamp DESC')
    logs = c.fetchall()
    conn.close()
    return render_template('logs.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
