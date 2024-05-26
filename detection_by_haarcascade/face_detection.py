import cv2

#Loading Cascade for face
face_cascade = cv2.CascadeClassifier("haar-cascade-files\haarcascade_frontalface_default.xml")


#Function to detect face
def detect_face(gray_frame, face_cascade):

    #Detecting face
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return faces

#Initializing the video capture
cap = cv2.VideoCapture(0)

while True:
    #Read the frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect face
    faces = detect_face(gray_frame,face_cascade)
    

    #Check if faces are detected
    if faces is not None:
        if len(faces) > 0:
            #Drawing a rectagle around detected eye
            for (x,y,w,h) in faces:
                frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        #Display the frame
        cv2.imshow('Face Detecction', frame)

        #Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#Release the capture
cap.release()
cv2.destroyAllWindows()