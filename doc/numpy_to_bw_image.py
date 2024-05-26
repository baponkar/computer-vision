import cv2
import numpy as np

height, width = 100, 100

image = np.zeros((height, width),dtype=np.uint8)

#Fill the image with gredient
for i in range(height):
    for j in range(width):
        image[i, j] = int((i + j) / (height + width) * 255)

# Displaying the image
cv2.imshow("Gredient Image", image)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()