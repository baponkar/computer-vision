import cv2

# Load Cascade for face and eye
face_cascade = cv2.CascadeClassifier("haar-cascade-files/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haar-cascade-files/haarcascade_eye.xml")


# Function to detect eye
def detect_eye(gray_frame, face_cascade, eye_cascade):
    # Detecting face
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30))

    # List to store eye coordinates
    eyes = []

    # Detecting eye for each face
    for (x, y, w, h) in faces:
        roi_gray = gray_frame[y:y + h, x:x + w]
        # Detect eyes within the face region
        detected_eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.05, minNeighbors=8, minSize=(20,20))
        # Convert eye coordinates to global coordinates
        for (ex, ey, ew, eh) in detected_eyes:
            #eyes.append((x + ex, y + ey, ew, eh)) #Store x,y,width,height
            eyes.append((x + ex + ew // 2, y + ey + eh // 2))  # Store center of the eye
    return eyes

# Initializing the video capture
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Detect eye
    eyes = detect_eye(gray_frame, face_cascade, eye_cascade)

    # Draw circles around the detected eyes
    for (x, y) in eyes:
        cv2.circle(frame, (x, y), 20, (0, 0, 255), 2)  # Change the radius as needed

    # Display the frame
    cv2.imshow('Face Detection', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
