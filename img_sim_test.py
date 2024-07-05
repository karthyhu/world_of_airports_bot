import cv2
import numpy as np
# Set the path to the images
image1_path = 'img/screenshot.png'
image2_path = 'img/main_event.png'
# image2_path = 'img/test.png'

# Load the images
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

print(image1.shape)


# Convert the images to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(gray1, gray2, cv2.TM_CCOEFF_NORMED) 

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val, max_loc)

color = (255, 255, 255)
thickness = 3

w = image2.shape[1]
h = image2.shape[0]


threshold = 0.85
yloc, xloc = np.where(result >= threshold)

for (x, y) in zip(xloc, yloc):
    cv2.rectangle(image1, (x, y), (x + w, y + h), color, thickness)

# cv2.rectangle(image1, max_loc, (max_loc[0] + w, max_loc[1] + h), color, thickness)

# Display the images
cv2.namedWindow("Image 1", cv2.WINDOW_NORMAL)
cv2.imshow("Image 1", image1)

cv2.waitKey(0)
cv2.destroyAllWindows()
