#Import libraries
import time
from datetime import datetime as dt

#Path to host file, redirect to local server
host_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.netflix.com", "www.facebook.com"]

#Condition
while True:
    #Check for current time
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Rihanna")

        #Open file and read the contents
        file = open(host_path, "r+")
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                #Write the IP of localhost and name of website to block
                file.write(redirect + " " + website + "\n")
    else:
        print("Drake")
