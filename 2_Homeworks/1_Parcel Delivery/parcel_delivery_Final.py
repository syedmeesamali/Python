import re
import sys

def get_input(regex, input_message=None, error_message=None, ignore_case=True):
    """Gets valid input, validated using regular expressions."""
    # loops until input is valid ("break" is called)
    while True:
        # input to validate, input prompt is as specified
        u_input = input(str(input_message))

        # check if the user wants to quit or cancel the order
        lower = u_input.lower()
        if lower == "qq" or lower == "quit":
            sys.exit()
        elif u_input == "cc" or u_input == "cancel":
            raise CancelOrder()

        # check if the input matches the regex provided
        if ignore_case:
            if re.match(regex, u_input, re.IGNORECASE):
                break
        else:
            if re.match(regex, u_input):
                break

        # if it doesn't match, and an error message has been specified
        if error_message:
            print(str(error_message))

    return u_input

def main():
    print("-----------------------------------");
    print("Welcome to Parcel Delivery System!");
    print("-----------------------------------");

    count=0         #Counter to take inputs from user
    accepted=0      #Keep track of inputs accepted fully
    rej=0           #Parcels rejected
    total_weight=0  #Total weight
    total_price=0   #Total price

    while True:
        test=str(input("Press (y) to continue or any key to end!"))
        if test!='y':
            break
        count=count+1
        x=int(get_input(r"\d+$","Please enter x-dimension of parcel # "+str(count)+": ","Only digits please!"))

        if x>80:
            rej+=1
            print("Parcel is REJECTED as x-dim ="+str(x)+" cm, which is more than 80cm limit")
            continue
            
        y=int(get_input(r"\d+$","Please enter y-dimension of parcel # "+str(count)+": ","Only digits please!"))
        if y>80:
            rej+=1
            print("Parcel is REJECTED as y-dim ="+str(y)+" cm, which is more than 80cm limit")
            continue
            
        z=int(get_input(r"\d+$","Please enter z-dimension of parcel # "+str(count)+": ","Only digits please!"))
        if z>80:
            rej+=1
            print("Parcel is REJECTED as z-dim ="+str(z)+" cm, which is more than 80cm limit")
            continue
            
        sum_xyz=x+y+z;
        if sum_xyz>200:
            rej+=1
            print("Parcel is REJECTED as x + y + z="+str(sum_xyz)+" cm, which is more than 200cm limit!")
            continue

        while True:
                weight=float(get_input(r"\d+\.\d+","Please enter weight (floating point) for Parcel # "+str(count)+": ","Only floating numbers from 1 to 10 please!"))
                
                if 0 < weight < 10:
                    if weight<=5:
                        price=10
                        total_price+=price
                        total_weight+=weight
                    else:
                        price=10+(weight-5)*1
                        total_price+=price
                        total_weight+=weight
                    break
                else:
                    print("Must be a digit, 1 or less than 10 (but more than 0)")        
                
        accepted+=1
        print("Parcel # "+str(count)+" is ACCEPTED for processing and dimensions are: "+str(sum_xyz)+" cm")

    print("\n---------------------------");
    print("-SUMMARY OF PARCEL DELIVERY-");
    print("---------------------------");
    print("\nA total of "+str(accepted)+" number(s) of parcels were ACCEPTED")
    print("Total weight of "+str(accepted)+" number(s) of parcels is: "+str(total_weight)+" Kg")
    print("Total price to send "+str(accepted)+" number(s) of parcels is: "+str(total_price)+" USD")
    print("A total of "+str(rej)+" number(s) of parcels were REJECTED")

main()
