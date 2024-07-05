import cv2
import pyautogui
import numpy as np

# Draw a square on the screenshot
start_point = (0, 30)
end_point = (1600, 935)
color = (0, 0, 255)
thickness = 3

# Take a screenshot
# screenshot = pyautogui.screenshot(region=(start_point[0], start_point[1], end_point[0], end_point[1]))
screenshot = pyautogui.screenshot()
screenshot = np.array(screenshot)
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

cv2.rectangle(screenshot, start_point, end_point, color, thickness)

# Display the screenshot
cv2.imshow("Screenshot", screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the screenshot
cv2.imwrite("img/screenshot.png", screenshot)
