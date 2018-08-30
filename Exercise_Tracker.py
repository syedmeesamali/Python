

def registration():
    print("-----------------------------------")
    print("Welcome to EXERCIZE TRACKER SYSTEM!")
    print("-----------------------------------")

    count = 0         #Counter to take inputs from user
    global user_name_first, user_name_last, age, height, weight
    global email_address, intensity, client_ID
    
    while True:
        test = str(input("Press (y) to continue or any key to end!"))
        if test != 'y':
            break
        count = count+1
    
        user_name_first = str(input("Please enter your first name: "))
        user_name_last = str(input("Please enter your last name: "))
        age = int(input("Please enter your age: "))
        height = int(input("Please enter your height in cm: "))
        weight = int(input("Please enter your weight in Kg: "))
        email_address = str(input("Please enter your email address:  "))
        intensity  =  str(input("Please enter Exercise intensity level (high or intense):  "))
        client_ID = (user_name_first[0:3] + user_name_last[-2:]).upper()
        
        #Print summary of input information    
        print("-----------------------------------")
        print("Below is SUMMARY of your REGISTRATION INFO")
        print("-----------------------------------")
        print("Your first name is: " + str(user_name_first))
        check1 = str(input("Press (c) to confirm or any key to edit!"))
        if check1 != 'c':
            user_name_first = str(input("Please enter your first name: "))
        print("Your last name is: " + str(user_name_last))    
        check1 = str(input("Press (c) to confirm or any key to edit!"))
        if check1 != 'c':
            user_name_last = str(input("Please enter your first name: "))
    
registration()

def print_Summary():
        print("-----------------------------------")
        print("Below is SUMMARY of your REGISTRATION INFO")
        print("-----------------------------------")
        print("Your name is: " + str(user_name_first) + " " + str(user_name_last))
        print("Your age is: " + str(age) + ", Height is:  " + str(height) + ", Weight is: " + str(weight) + " Kgs")
        print("Your email address is: " + str(email_address))
        print("Intensity of Exercise chosen is: " + str(intensity))
        print("We have assigned you Client-ID # " + str(client_ID))

print_Summary()