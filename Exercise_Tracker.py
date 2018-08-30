def main():
    print("-----------------------------------")
    print("Welcome to EXCERSIZE TRACKER SYSTEM!")
    print("-----------------------------------")

    count = 0         #Counter to take inputs from user
    
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
        client_ID = user_name_first[0:3] + user_name_last[-2:]
        
        #Print the customer ID
        print("Your Assigned Customer_ID is  = "+ str(client_ID))
        

main()