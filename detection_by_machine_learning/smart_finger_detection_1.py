import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# Function to check if a finger is open or closed
def is_finger_open(landmarks, finger_tip_idx, finger_mcp_idx):
    return landmarks[finger_tip_idx].y < landmarks[finger_mcp_idx].y

# Function to check if the thumb is open or closed
def is_thumb_open(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks[mp_hands.HandLandmark.THUMB_IP]
    thumb_mcp = landmarks[mp_hands.HandLandmark.THUMB_MCP]
    thumb_cmc = landmarks[mp_hands.HandLandmark.THUMB_CMC]
    
    # Compute the vector from thumb tip to thumb CMC
    thumb_tip_to_cmc = np.array([thumb_tip.x - thumb_cmc.x, thumb_tip.y - thumb_cmc.y])
    
    # Compute the vector from thumb MCP to thumb CMC
    thumb_mcp_to_cmc = np.array([thumb_mcp.x - thumb_cmc.x, thumb_mcp.y - thumb_cmc.y])
    
    # Compute the angle between these two vectors
    angle = np.arccos(np.dot(thumb_tip_to_cmc, thumb_mcp_to_cmc) / 
                      (np.linalg.norm(thumb_tip_to_cmc) * np.linalg.norm(thumb_mcp_to_cmc)))
    
    # Convert angle from radians to degrees
    angle_degrees = np.degrees(angle)
    
    return angle_degrees > 45  # Adjust threshold as needed

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the image horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get landmarks
            landmarks = hand_landmarks.landmark
            
            # Check if each finger is open
            fingers = []
            fingers.append(is_thumb_open(landmarks))
            fingers.append(is_finger_open(landmarks, mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.INDEX_FINGER_MCP))
            fingers.append(is_finger_open(landmarks, mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_MCP))
            fingers.append(is_finger_open(landmarks, mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_MCP))
            fingers.append(is_finger_open(landmarks, mp_hands.HandLandmark.PINKY_TIP, mp_hands.HandLandmark.PINKY_MCP))
            
            # Count open fingers
            open_fingers = fingers.count(True)
            
            # Display the number of open fingers
            cv2.putText(frame, f'Open Fingers: {open_fingers}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
