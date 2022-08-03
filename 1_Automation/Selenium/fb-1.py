from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def main():
    # Your Facebook account user and password
    usr = "enmail@gmail.com"
    pwd = "some_pass"
    grp = ['https://www.facebook.com/groups/521001902330400/', 'https://www.facebook.com/groups/grpid/']
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.notifications": 2  # 1:allow, 2:block
    })

    driver = webdriver.Chrome(executable_path='D:/SYED/data/chromedriver.exe')
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
    for group in grp:
        driver.get(group)
        try:
            try:
                commentr = WebDriverWait(driver,10).until(EC.element_to_be_clickable( (By.XPATH, "//*[@name='xhpc_message_text']") ))
                commentr.click()
            except Exception:
                commentr = WebDriverWait(driver,10).until(EC.element_to_be_clickable( (By.XPATH, "//*[@loggingname='status_tab_selector']") ))
                commentr.click()
            commentr = WebDriverWait(driver,10).until(EC.element_to_be_clickable( (By.XPATH, "//*[@class='_3u15']") ))
            commentr.click()
            time.sleep(3)
            l = driver.find_elements_by_tag_name('input') 
            time.sleep(3)
            for g in l: 
                if g==driver.find_element_by_xpath("//input[@type='file'][@class='_n _5f0v']"): 
                    time.sleep(1)
                    g.send_keys(ipath) 
                    print('Image loaded')
            time.sleep(10)
            driver.find_element_by_xpath("//*[@class='_1mf _1mj']").send_keys(message)
            time.sleep(3)
            buttons = driver.find_elements_by_tag_name("button")
            time.sleep(3)
            for button in buttons:
                if button.text == "Post":
                    time.sleep(5)
                    button.click()
                    time.sleep(10)
        except Exception:
            pass
            print ('Image not posted in: '+ group)
    #driver.close()
if __name__ == '__main__':
    main()