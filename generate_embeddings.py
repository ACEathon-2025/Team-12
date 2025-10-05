import os
import sqlite3
import pickle
from deepface import DeepFace
import numpy as np


conn = sqlite3.connect('database/faces.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS known_faces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    embedding BLOB NOT NULL
)
''')
conn.commit()

def image_to_embedding(image_path):
    # Use DeepFace to get embeddings
    embeddings = DeepFace.represent(image_path, model_name='Facenet',enforce_detection=False)
    if embeddings:
        # embeddings is a list of dicts with 'embedding' key
        return embeddings[0]['embedding']
    return None

known_faces_folder = 'known_faces'

for person_name in os.listdir(known_faces_folder):
    person_folder = os.path.join(known_faces_folder, person_name)
    if not os.path.isdir(person_folder):
        continue

    embeddings = []
    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)
        embedding = image_to_embedding(image_path)
        if embedding is not None:
            embeddings.append(embedding)

    if embeddings:
        avg_embedding = np.mean(embeddings, axis=0)
        embedding_blob = pickle.dumps(avg_embedding)
        c.execute('DELETE FROM known_faces WHERE name=?', (person_name,))
        c.execute('INSERT INTO known_faces (name, embedding) VALUES (?, ?)', (person_name, embedding_blob))
        conn.commit()
        print(f'Stored embeddings for {person_name}')

conn.close()
