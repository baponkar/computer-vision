import cv2
import numpy as np

# Function to detect hand
def detect_hand(frame):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of skin color in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Threshold the HSV image to get only skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Find contours in the masked image
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the maximum area (assuming it's the hand)
    max_contour = max(contours, key=cv2.contourArea)

    # Return the bounding box of the hand
    x, y, w, h = cv2.boundingRect(max_contour)
    return x, y, w, h

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    # Read frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Detect hand
    x, y, w, h = detect_hand(frame)

    # Draw rectangle around the hand region
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Hand Tracking', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture
cap.release()
cv2.destroyAllWindows()
