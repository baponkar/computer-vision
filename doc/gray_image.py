'''Thre way to make gray scale image'''

# import opencv 
import cv2 

# Load the input image 
image = cv2.imread('images/old_city.jpg') 
cv2.imshow('Original', image) 
cv2.waitKey(0) 

# Use the cvtColor() function to grayscale the image 
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray_image =  cv2.imread('images/old_city.jpg', 0) #directly read as gray image

#getting width and height
gray_image = image
height, width = image.shape[0:2]
for row in range(height):
    for col in range(width):
        # Find the average of the BGR pixel values 
        gray_image[row, col] = sum(image[row,col]) / 3


cv2.imshow('Grayscale', gray_image) 
cv2.waitKey(0) 

# Window shown waits for any key pressing event 
cv2.destroyAllWindows()
