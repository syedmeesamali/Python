import pyautogui, time
time.sleep(2)

pyautogui.click(800,950)
#pyautogui.click(1210,715)

y = 321
clickCount = 0
for i in range(12, 30, 1):
    try:
        if i > 11:      
            clickCount = clickCount + 1
            im=pyautogui.screenshot(region=(50,5,1000,700))
            im.save('img' + str(i) + '.png')
            time.sleep(3)
            pyautogui.click(522,60)  #Click elev button
            for x in range(clickCount):
                pyautogui.click(608, 466)  #Click down
            pyautogui.click(554, 466)  #Click storey
            pyautogui.click(706, 468)  #Click OK Button
            time.sleep(2)
        else:
            im=pyautogui.screenshot(region=(50,5,1000,700))
            im.save('img' + str(i) + '.png')
            time.sleep(3)
            y = y + 13
            pyautogui.click(522,60)  #Click elev button
            pyautogui.click(560,y)  #Click storey
            pyautogui.click(706, 468)  #Click OK Button
            time.sleep(2)

    except IOError:
        if i > 11:
            clickCount = clickCount + 1
            im=pyautogui.screenshot(region=(50,5,1000,700))
            im.save('img' + str(i) + '.png')
            time.sleep(3)
            pyautogui.click(522,60)  #Click elev button
            for x in range(clickCount):
                pyautogui.click(608, 466)  #Click down
            pyautogui.click(554, 466)  #Click storey
            pyautogui.click(706, 468)  #Click OK Button
            time.sleep(2)
        else:
            im=pyautogui.screenshot(region=(50,5,1000,700))
            im.save('img' + str(i) + '.png')
            time.sleep(3)
            y = y + 13
            pyautogui.click(522,60)  #Click elev button
            pyautogui.click(560,y)  #Click storey
            pyautogui.click(706, 468)  #Click OK Button
            time.sleep(2)
        #pyautogui.click(1210,715) Move forward button