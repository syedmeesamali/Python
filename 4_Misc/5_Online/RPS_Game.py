def name_to_number(num):
    if num == "rock":
        return 0
    elif num == "Spock":
        return 1
    elif num == "paper":
        return 2
    elif num == "lizard":
        return 3
    elif num == "scissors":
        return 4
    else:
        return "ERROR!"

def number_to_name(numb):
    if numb == 0:
        return "rock"
    elif numb == 1:
        return "Spock"
    elif numb == 2:
        return "paper"
    elif numb == 3:
        return "lizard"
    elif numb == 4:
        return "scissors"
    else:
        return "ERROR!"

def rpsls(player_choice):
    print()
    if player_choice == 1:
        print("You choose Name to Number Game!")
        x = input("Enter name? ")
        print(name_to_number(x))
    elif player_choice == 2:
        print("You choose Number to Name Game!")
        x = input("Enter number? ")
        print(number_to_name(int(x)))
    else:
        print("Bye have a good day!")
n = int(input("Enter choice.. "))
rpsls(n)