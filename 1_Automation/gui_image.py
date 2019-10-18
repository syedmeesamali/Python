import pyscreenshot as ImageGrab
import pyautogui, time
time.sleep(2)

pyautogui.click(800,950)
#pyautogui.click(1210,715)

def main():
#part of the screen to be captured
    for i in range(4):
        im = ImageGrab.grab(bbox=(10,100,1000,700))
        time.sleep(1)
        im.save('im' + str(i) + '.png')
        pyautogui.click(800,950)
        time.sleep(1)

if __name__ == '__main__':
    main()
