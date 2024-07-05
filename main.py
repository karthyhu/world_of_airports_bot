import cv2
import pyautogui
import numpy as np
from time import sleep


main_event_path = 'img/main_event.png'
choos_stand_path = 'img/choos_stand.png'
base_point_path = 'img/base_point.png'
allow_landing_path = 'img/allow_landing.png'
add_number_path = 'img/add_number.png'
start_path = 'img/start.png'
done_path = 'img/done.png'
get_award_path = 'img/get_award.png'
extend_contract_path = 'img/extend_contract.png'
just_fucking_press_path = 'img/just_fucking_press.png'
take_over_path = 'img/take_over.png'
pull_up_path = 'img/pull_up.png'
fly_path = 'img/fly.png'
check_member_limit_path = 'img/check_member_limit.png'

screenshot = pyautogui.screenshot()

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

def check_clolor(x,y,range_start):
    # Load the images
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    img = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    region = screenshot[y:y+5, x:x+5]

    # cv2.rectangle(img, (x, y), (x+5,y+5), (255, 5, 65), 3)
    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 將該區塊轉換為numpy數組以便分析
    region_np = np.array(region)

    # 計算該區塊的平均顏色
    average_color = np.mean(region_np, axis=(0, 1))
    # if average_color[2] == 123.0:
    #     cv2.rectangle(img, (x, y), (x+5,y+5), (255, 5, 65), 3)
    #     cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    #     cv2.imshow('image', img)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    # print(average_color[2])
    if average_color[2] > range_start-1 and average_color[2] < range_start+1:
        ret =  True
    else:
        ret =  False
    return ret, average_color[2]


base_point = (0, 0)
bottom_1 = (297,-743)
bottom_2 = (-210,-580)
check_clolor_b = (288,-658)
while True:
    # sleep(5)

    ret, x, y, unuse = check_sim(base_point_path)
    base_point = (x, y)
    # pyautogui.moveTo(x, y-60)
    # pyautogui.click()

    ret, x, y, all_event = check_sim(main_event_path)
    if ret:
        sleep(0.2)
        for (x, y) in zip(all_event[0], all_event[1]):
            pyautogui.moveTo(x, y)
            pyautogui.click()

            sleep(0.2)
            ret, x, y, unuse = check_sim(choos_stand_path)
            if ret:
                sleep(0.2)
                pyautogui.moveTo(x, y)
                pyautogui.click()   #選擇
                sleep(0.2)
                pyautogui.click()   #確認

            ret, x, y, unuse = check_sim(add_number_path)
            if ret:
                pyautogui.moveTo(x, y)
                while True:
                    pyautogui.click()
                    sleep(0.2)
                    limit, tx, ty, unuse = check_sim(check_member_limit_path)
                    full ,unused = check_clolor(x, y, 165)
                    if limit == True:
                        mem_is_limit = True
                        break
                    if full == True:
                        mem_is_limit = False
                        break

                if mem_is_limit == False:
                    pyautogui.moveTo(x-15, y+70)  #移動到"開始處裡"
                    pyautogui.click()
                    # print("add member")
                # else:
                #     pyautogui.moveTo(x+50, y-20)  #跳出畫面
                #     pyautogui.click()
                continue                
                


            ret, x, y, unuse = check_sim(allow_landing_path)
            if ret:
                sleep(0.2)
                pyautogui.moveTo(x, y)
                pyautogui.click()  
                sleep(0.2) 
                pyautogui.click()   

            while True:
                ret, x, y, unuse = check_sim(start_path)
                if ret:
                    sleep(0.2)
                    pyautogui.moveTo(x, y)
                    pyautogui.click()   
                else:
                    break

            ret, x, y, unuse = check_sim(done_path)
            if ret:
                sleep(0.2)
                pyautogui.moveTo(x, y)
                pyautogui.click()   #選擇
                sleep(0.2)
                pyautogui.click()   #確認
                break

            ret, x, y, unuse = check_sim(extend_contract_path)
            if ret:
                sleep(0.2)
                pyautogui.moveTo(x, y)
                pyautogui.click()
                break
            
            ret ,unused= check_clolor(base_point[0] - bottom_1[0],base_point[1] - bottom_1[1], 220)
            # print("bottom_1  = ",unused)
            if ret:
                print("bottom_1 click")
                pyautogui.moveTo(base_point[0] - bottom_1[0],base_point[1] - bottom_1[1])
                pyautogui.click()
                break

    else:
        sleep(5)
    
    ret ,unused= check_clolor(base_point[0] - bottom_2[0],base_point[1] - bottom_2[1], 220)
    # print("bottom_2  = ",unused)
    if ret:
        pyautogui.moveTo(base_point[0] - bottom_2[0],base_point[1] - bottom_2[1])
        pyautogui.click()




    
