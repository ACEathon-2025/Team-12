from PIL import Image
import numpy as np
import face_recognition

image_path = "known_faces/Abhiram/img_1.jpg"
 # change as needed

# Always use PIL to read and convert to RGB, then to 'uint8' numpy array
pil_image = Image.open(image_path).convert('RGB')
image = np.asarray(pil_image, dtype=np.uint8)

print("Shape:", image.shape)
print("Dtype:", image.dtype)
print("NDIM:", image.ndim)
print("Unique values (channels):", image[...,0].min(), image[...,0].max())

try:
    face_locations = face_recognition.face_locations(image)
    print("Found faces:", face_locations)
except Exception as e:
    print("ERROR:", repr(e))
