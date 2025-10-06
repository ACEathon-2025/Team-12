import sqlite3
import pickle
import numpy as np
from deepface import DeepFace
from sklearn.metrics.pairwise import cosine_similarity

def get_known_embeddings():
    conn = sqlite3.connect('database/faces.db')
    c = conn.cursor()
    c.execute("SELECT name, embedding FROM known_faces")
    data = c.fetchall()
    conn.close()
    known = []
    for name, emb_blob in data:
        emb = pickle.loads(emb_blob)
        known.append((name, emb))
    return known

def recognize_face(image_path, known_embeddings, threshold=0.85):
    result = DeepFace.represent(image_path, model_name='Facenet', enforce_detection=False)
    if not result:
        print("No face found in input image.")
        return None
    input_embedding = np.array(result[0]['embedding']).reshape(1, -1)
    best_match = None
    best_similarity = 0  # cosine similarity ranges [0,1]
    for name, emb in known_embeddings:
        emb_array = np.array(emb).reshape(1, -1)
        similarity = cosine_similarity(input_embedding, emb_array)[0][0]
        if similarity > best_similarity and similarity > threshold:
            best_similarity = similarity
            best_match = name
    if best_match:
        print(f"Recognized {best_match} with similarity {best_similarity}")
        return best_match
    else:
        print("No match found.")
        return None


# ------- USAGE -------
if __name__ == '__main__':
    # Path to the test image (change to your test file)
    test_image_path = "test_image.jpg"
    known_embeddings = get_known_embeddings()
    recognize_face(test_image_path, known_embeddings)
