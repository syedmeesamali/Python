import pyscreenshot as ImageGrab
import pyautogui, time
time.sleep(4)

pyautogui.click(800,950)
time.sleep(2)
def main():
#part of the screen to be captured
    im = ImageGrab.grab(bbox=(10,100,1000,700))
    #im.show()
    im.save('im.png')

if __name__ == '__main__':
    main()
