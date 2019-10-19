import pyautogui, time
import winsound
time.sleep(2)

pyautogui.click(250,950)
#pyautogui.click(1210,715)

clickCount = 0
for i in range(37):
    try:
        im=pyautogui.screenshot(region=(400,5,950,700))
        im.save('_V22_' + str(i) + '.png')
        time.sleep(0.8)
        pyautogui.click(1210,715)  #Click elev button
        time.sleep(0.5)
        pyautogui.click(1210,715)  #Click elev button
        time.sleep(0.4)
    except IOError:
        im=pyautogui.screenshot(region=(400,5,950,700))
        im.save('_V22_' + str(i) + '.png')
        time.sleep(0.8)
        pyautogui.click(1210,715)  #Click elev button
        time.sleep(0.5)
        pyautogui.click(1210,715)  #Click elev button
        time.sleep(0.4)

frequency = 6000  # Set Frequency To 2500 Hertz
duration = 3000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)