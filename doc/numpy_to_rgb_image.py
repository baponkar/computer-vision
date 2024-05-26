import numpy as np
import matplotlib.pyplot as plt

# Create a 100x100 pixel color image with a gradient
height, width = 100, 100
image = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the image with a gradient
for i in range(height):
    for j in range(width):
        image[i, j] = [int(i / height * 255), int(j / width * 255), 128]  # Red and Green gradients, Blue constant

# Display the image
plt.imshow(image)
plt.axis('off')  # Hide the axis
plt.show()

# Save the image
plt.imsave('color_gradient_image.png', image)
