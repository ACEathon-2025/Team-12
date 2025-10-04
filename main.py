import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Webcam Live Feed', frame)

    # Exit if 'q' key is pressed or window is closed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Check if window is closed
    if cv2.getWindowProperty('Webcam Live Feed', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
