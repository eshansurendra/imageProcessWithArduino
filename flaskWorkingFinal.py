import os
import sqlite3
import csv
from flask import Flask, request, jsonify

app = Flask(__name__)

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Create or connect to the database in the current directory
db_path = os.path.join(current_directory, 'text_database.db')
db_connection = sqlite3.connect(db_path)
db_cursor = db_connection.cursor()

# Create a table to store text values
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS texts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT
    )
''')
db_connection.commit()

@app.route('/store_text', methods=['POST'])
def store_text():
    new_text = request.form.get('text')
    insert_text_into_database(new_text)
    insert_text_into_csv(new_text)
    return jsonify({'message': 'Text stored'})

@app.route('/get_text', methods=['GET'])
def get_text():
    stored_text = retrieve_text_from_database()
    return jsonify({'text': stored_text})

def insert_text_into_database(text):
    db_cursor.execute('INSERT INTO texts (text) VALUES (?)', (text,))
    db_connection.commit()

def retrieve_text_from_database():
    db_cursor.execute('SELECT text FROM texts ORDER BY id DESC LIMIT 1')
    result = db_cursor.fetchone()
    if result:
        return result[0]
    return ''

def insert_text_into_csv(text):
    csv_path = os.path.join(current_directory, 'text_data.csv')
    with open(csv_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([text])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
