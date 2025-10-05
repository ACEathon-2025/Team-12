import cv2
import os

def capture_faces(person_name):
    folder_path = os.path.join('known_faces', person_name)
    os.makedirs(folder_path, exist_ok=True)

    cap = cv2.VideoCapture(0)
    cv2.namedWindow(f'Capture Images for {person_name}')

    print("Press 'c' to capture image, 'q' to quit.")

    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow(f'Capture Images for {person_name}', frame)

        k = cv2.waitKey(1)
        if k & 0xFF == ord('q'):
            print("Quitting...")
            break
        elif k & 0xFF == ord('c'):
            img_name = f"img_{count+1}.jpg"
            img_path = os.path.join(folder_path, img_name)
            cv2.imwrite(img_path, frame)
            print(f"{img_name} saved!")
            count += 1

    cap.release()
    cv2.destroyAllWindows()
    print(f"Captured {count} images for {person_name} in {folder_path}")

if __name__ == '__main__':
    person = input("Enter the person's name: ")
    capture_faces(person)
