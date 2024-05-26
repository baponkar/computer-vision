import cv2
import numpy as np

# Load Haarcascade XML files
face_cascade = cv2.CascadeClassifier('haar-cascade-files\haarcascade_frontalface_default.xml')
hand_cascade = cv2.CascadeClassifier('haar-cascade-files\hand.xml')

def detect_skin(frame):
    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the skin color range in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    
    # Create a mask for skin color
    skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    return skin_mask

def main():
    # Start video capture
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect skin
        skin_mask = detect_skin(frame)
        skin = cv2.bitwise_and(frame, frame, mask=skin_mask)

        # Detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Cancel faces from skin detection mask
        for (fx, fy, fw, fh) in faces:
            cv2.rectangle(skin_mask, (fx, fy), (fx + fw, fy + fh), (0, 0, 0), -1)  # Black out face area in the skin mask

        # Detect hands
        hands = hand_cascade.detectMultiScale(gray, 1.1, 4)
        
        # Draw rectangles around detected faces and hands
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        for (x, y, w, h) in hands:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('Frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
