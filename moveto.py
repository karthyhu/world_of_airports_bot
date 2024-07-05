import pyautogui
from time import sleep
import numpy as np
import cv2

def check_clolor(x,y,range_start):
    # Load the images
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    img = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    region = screenshot[y:y+10, x:x+10]

    # cv2.rectangle(img, (x, y), (x+10,y+10), (255, 5, 65), 3)
    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 將該區塊轉換為numpy數組以便分析
    region_np = np.array(region)

    # 計算該區塊的平均顏色
    average_color = np.mean(region_np, axis=(0, 1))
    print(average_color[2])
    if average_color[2] > range_start-1 and average_color[2] < range_start+1:
        return True
    else:
        return False

def check_sim(image2_path):
    # sleep(0.5)
    ret = False

    # Load the images
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    image2 = cv2.imread(image2_path)
    
    # Convert the images to grayscale
    gray1 = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
    result = cv2.matchTemplate(gray1, gray2, cv2.TM_CCOEFF_NORMED) 
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.85
    if max_val >= threshold:
        ret = True
    # print(max_val, max_loc)
    
    color = (255, 0, 255)
    thickness = 3
    
    w = image2.shape[1]
    h = image2.shape[0]
    
    

    yloc, xloc = np.where(result >= threshold)

    
    # for (x, y) in zip(xloc, yloc):
    #     cv2.rectangle(screenshot, (x, y), (x + w, y + h), color, thickness)

    # Display the images
    # cv2.namedWindow(str(image2_path[4:-4]), cv2.WINDOW_NORMAL)
    # cv2.imshow(str(image2_path[4:-4]), screenshot)
    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow('image', screenshot)
    # cv2.waitKey(2)
    # cv2.destroyAllWindows()
    # sleep(0.1)
    # return ret, int(target_x)+w, int(target_y)+h
    return ret, max_loc[0] + w, max_loc[1] + h, (xloc, yloc)


base_point_path = 'img/base_point.png'

ret, x, y, unuse = check_sim(base_point_path)
pyautogui.moveTo(x, y)
print(x, y)

bottom1 = 297,-743
bottom2 = -210,-580
bottom3 = 288,-658

# 572,101

# 284,759 123 165


pyautogui.moveTo(x-bottom3[0], y-bottom3[1])
check_clolor(x-bottom3[0], y-bottom3[1], 0)
