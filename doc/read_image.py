# Importing the OpenCV library
import cv2

# Reading the image
image = cv2.imread('./images/road_with_cars.jpg')
#image = cv2.imread('./images/road_with_cars.jpg', cv2.IMREAD_GRAYSCALE)

# Extracting the height and width of an image
h, w = image.shape[:2]

print("Height = {}, Width = {}".format(h, w)) #735x1100

#Getting RGB value for pixel 100,100

(B,G,R) = image[100,100]

#Displaying pixel value
print("R={},G={},B={}".format(R,G,B)) #R=239,G=200,B=157

# We can also pass the channel to extract
# the value for a specific channel
B = image[100, 100, 2]
print("B = {}".format(B))

# We will calculate the region of interest
# by slicing the pixels of the image
#roi = image[100 : 500, 200 : 700]
roi = image[100 : 150, 100 : 500]
#cv2.imshow("ROI", roi)
#cv2.waitKey(0)


# resize() function takes 2 parameters,
# the image and the dimensions
#resize = cv2.resize(image, (500, 500))
#cv2.imshow("Resized Image", resize)
#cv2.waitKey(0)

# Using the rectangle() function to create a rectangle.
rectangle = cv2.rectangle(image, (500, 300),(600, 400), (255, 0, 0), 2)

# Using the circle function to create a circle
circle = cv2.circle(image, (500, 300), 20, (0, 0, 255), 2)
circle1 = cv2.circle(image, (600, 400), 20, (0, 0, 255), 2)

# Adding the text using putText() function
text = cv2.putText(image, 'OpenCV Demo', (500, 300), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)

# Calculating the ratio
ratio = 400 / w
print("Ratio={}".format(ratio))
# Creating a tuple containing width and height
dim = (400, int(h * ratio))
# Resizing the image
resize_aspect = cv2.resize(image, dim)
#cv2.imshow("Resized Image", resize_aspect)
#cv2.waitKey(0)

import numpy as np
import matplotlib.pyplot as plt

plt.imshow(image)

#hold the window
#plt.waitforbuttonpress()
#plt.close('all')

B, G, R = cv2.split(image) 
# Corresponding channels are separated 
  
cv2.imshow("original", image) 
cv2.waitKey(0) 
  
cv2.imshow("blue", B) 
cv2.waitKey(0) 
  
cv2.imshow("Green", G) 
cv2.waitKey(0) 
  
cv2.imshow("red", R) 
cv2.waitKey(0) 
  
cv2.destroyAllWindows()