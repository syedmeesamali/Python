import pyautogui, time
import winsound #Buzzer sound to notify when the program ends
time.sleep(2) #Initial lag time
pyautogui.click(120,750) #This will activate the software window

for i in range(5):
    #Try-catch ensures dealing with unforeseen circumstances during actual execution
    try:
        #In the region argument below, first two numbers are x and y coordinates of start of capture
        #and next two numbers are size of image i.e. x and y size
        im=pyautogui.screenshot(region=(375,0,1145,700))
        im.save('V22_' + str(i) + '.png') #Use a numbering scheme that is quite intuitive
        time.sleep(0.5)
        pyautogui.click(1210,715)  #Click the next button
        time.sleep(0.8)
    except IOError:
        im=pyautogui.screenshot(region=(375,0,1145,700))
        im.save('V22_' + str(i) + '.png')
        time.sleep(0.5)
        pyautogui.click(1210,715)
        time.sleep(0.8)
frequency = 4000  # Set Frequency To 4000 Hertz
duration = 3000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)