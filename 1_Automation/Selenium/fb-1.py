import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

user = "mail@gmail.com"
passwd = "pas23"
s = Service('D:\SYED\data\chromedriver.exe')
driver = webdriver.Chrome(service=s)

def login(usr, pwd):    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.notifications": 2  # 1:allow, 2:block
    })
    driver.implicitly_wait(15)  # seconds
    # Go to facebook.com
    driver.get("http://www.facebook.com")
    time.sleep(2)
    elem = driver.find_element("name", "email")       # Enter user email
    elem.send_keys(usr)
    elem = driver.find_element("name", "pass")        # Enter user password
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)
    time.sleep(10)


def post_content(post):
    time.sleep(3) ## A 3 second break in the program so that everythin loads perfectly
    new WebDriverWait(driver, 10).until(EC.elementToBeClickable(By.xpath("//div[text()='Sign Up']//ancestor::div[1]//preceding-sibling::img[1]"))).click();
    driver.send_keys("Hello World of FB")
    time.sleep(3) ## A 3 second break in the program so that everythin loads perfectly
    actions= ActionChains(driver) ##Action Chains
    actions.send_keys(Keys.TAB)  ##Press TAB
    actions.send_keys(Keys.ENTER) ##Press ENTER
    actions.send_keys(post)
    actions.send_keys(Keys.TAB * 10)  ### Press TAB 10 Times to reach POST button
    actions.send_keys(Keys.ENTER) ### Press ENTER to post the content on facebook
    actions.perform()  ## To perfrom all the operations in the action chains
    pass

def main():
    login(user, passwd)
    try:
        post_content('Hello from fb')
    except Exception:
        pass
        print('Image not posted!')
#driver.close()
if __name__ == '__main__':
    main()