import cv2
import numpy as np

image_path = './images/road_with_cars.jpg'

#loading image with cv2
image = cv2.imread(image_path) #Loading BGR colored image

#Converting BGR to RGB image
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Define scale factor
zoom_in_factor = 3.0 #increasing size
zoom_out_factor = 1/3.0 #decresing size

#Get the original width and height
height, width = image_rgb.shape[0:2]


#calculating dimension for zoomed in image
zoom_in_height = int(height * zoom_in_factor)
zoom_in_width = int(width * zoom_in_factor)

#Resize image
zoom_in_image = cv2.resize(src=image_rgb, dsize=(zoom_in_width, zoom_in_height), interpolation=cv2.INTER_AREA)


#calculating dimension for zoomed out image
zoom_out_height = int(height * zoom_out_factor)
zoom_out_width = int(width * zoom_out_factor)

#Resize image
zoom_out_image = cv2.resize(src=image_rgb, dsize=(zoom_out_width, zoom_out_height), interpolation=cv2.INTER_AREA)

#Showing Zoomed in or out image
cv2.imshow("3X Zoom In Image", zoom_out_image)
# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
	

