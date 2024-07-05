import pyautogui
from time import sleep
import numpy as np
import cv2

def check_clolor(x,y,range_start):
    # Load the images
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    img = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    region = screenshot[y:y+5, x:x+5]

    # cv2.rectangle(img, (x, y), (x+10,y+10), (255, 5, 65), 3)
    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 將該區塊轉換為numpy數組以便分析
    region_np = np.array(region)

    # 計算該區塊的平均顏色
    average_color = np.mean(region_np, axis=(0, 1))
    print(average_color)
    if average_color[2] > range_start-1 and average_color[2] < range_start+1:
        return True
    else:
        return False
    


while True:
    # Get the current mouse position
    x, y = pyautogui.position()
    check_clolor(x,y, 0)

    # Print the coordinates
    print(f"Mouse coordinates: ({x}, {y})")
    

    sleep(1)