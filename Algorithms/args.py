#CSEC 471 - Penetration Testing
#Homework 2 - Python Scripting
#Shereena AlFaheem

#libraries imported
from art import tprint
import argparse

#prints homework title in large styled format
tprint("homework2")

parser = argparse.ArgumentParser(add_help=False)

subparser = parser.add_subparsers(dest='command')
direct = subparser.add_parser('direct')
parser.add_argument('-v', '--version', action='version',
                    version='This %(prog)s program is currently running on Version 1.0')
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='You can either run this program directly or pass user input through the direct positional argument.')

direct.add_argument('--yourname', type=str, required=True, help="Name for user")
direct.add_argument('--start', type=int, required=True, help="Start Value")
direct.add_argument('--end', type=int, required=True, help="End Value")         
args = parser.parse_args()

if args.command == 'direct':
    for x in range(1,100):
        if x >= args.start and x <= args.end:
          print(f"{x}: {args.yourname} ")
    exit()
else:
    pass

while True:
    name = input("Enter your name: ")
    if name.isalpha():
        break
    print("Please enter alphabetical characters only")

startnumber = 0

#Function to get the starting number.
def get_startnum():
    while True:  
        try:    
            startnum = int(input("Enter a starting number between 0 and 99: "))
            val_1 = startnum
            if (val_1 > 0) and (val_1 < 99):
                break
            else:
                print("Enter a starting number between 0 and 99: \n")
                continue
        except ValueError:
            print("Amount must be a number, try again")
    startnumber = startnum
    return startnumber

#Function to get the ending number.
def get_endnum():
    while True:
        try:
            endnum = int(input("Enter an ending number between " + str(val_start) + " and 99: "))
            val = int(endnum)
            if val >= int(startnumber):
                break
            else:
                print("Number can't be less than the starting number, try again \n")
        except ValueError:
            print("Amount must be a number, try again")
    endnumber = endnum
    return endnumber

val_start = get_startnum()
val_end = get_endnum()

#Loop to print the number with name
for x in range(1,100):
    if x >= val_start and x <= val_end:
      print(f"{x}: {name}")
    else:
      print(f"{x}")

#Obsolete
def name_to_num():
    for x in range(1,100):
        if x >= args.start and x <= args.end:
          print(f"{x}: {name}")