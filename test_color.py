import cv2
import pyautogui
import numpy as np
from time import sleep

def check_clolor():
    # Load the images
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    img = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    # 選取特定區塊，這裡以左上角為(100, 100)，寬高為(50, 50)的區塊為例
    boxx = 166
    boxy = 845
    region = screenshot[boxy:boxy+10, boxx:boxx+10]
    img1 = cv2.cvtColor(region, cv2.COLOR_RGB2BGR)


    # cv2.rectangle(img, (boxx, boxy), (boxx+10,boxy+10), (255, 5, 65), 3)
    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imshow('image', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 將該區塊轉換為numpy數組以便分析
    region_np = np.array(region)

    # 計算該區塊的平均顏色
    average_color = np.mean(region_np, axis=(0, 1))
    print(average_color)
    if average_color[2] > 30 and average_color[2] < 40:
        return True
    else:
        return False


check_clolor()