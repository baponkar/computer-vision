import cv2
from mtcnn.mtcnn import MTCNN

# Initialize MTCNN detector
detector = MTCNN()

# Function to detect eyes and draw circles on pupils
def detect_and_draw_pupils(frame, faces):
    for face in faces:
        # Extract the bounding box and key points
        bounding_box = face['box']
        keypoints = face['keypoints']

        # Draw the bounding box
        cv2.rectangle(frame,
                      (bounding_box[0], bounding_box[1]),
                      (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                      (0, 155, 255),
                      2)

        # Draw circles on the eyes
        left_eye = keypoints['left_eye']
        right_eye = keypoints['right_eye']
        cv2.circle(frame, left_eye, 2, (0, 255, 0), 2)
        cv2.circle(frame, right_eye, 2, (0, 255, 0), 2)

        # Assuming pupils are near the center of the eyes for simplicity
        # For more accurate pupil detection, further processing is needed
        pupil_left = (left_eye[0], left_eye[1])
        pupil_right = (right_eye[0], right_eye[1])
        cv2.circle(frame, pupil_left, 2, (255, 0, 0), 2)
        cv2.circle(frame, pupil_right, 2, (255, 0, 0), 2)

    return frame

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the image horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Detect faces
    faces = detector.detect_faces(frame)

    # Detect and draw pupils
    frame = detect_and_draw_pupils(frame, faces)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
