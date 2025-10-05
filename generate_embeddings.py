import os
import sqlite3
import numpy as np
import face_recognition
import pickle

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
    from PIL import Image
    import numpy as np
    # Load image with PIL and convert to RGB explicitly
    pil_image = Image.open(image_path).convert('RGB')
    
    # Convert to numpy array with 'uint8' type
    image = np.asarray(pil_image, dtype=np.uint8)
    
    # Confirm image is 3-channel RGB
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("Image is not in RGB format")
    
    face_locations = face_recognition.face_locations(image)
    if len(face_locations) == 0:
        return None
    embedding = face_recognition.face_encodings(image, known_face_locations=face_locations)[0]
    return embedding




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
