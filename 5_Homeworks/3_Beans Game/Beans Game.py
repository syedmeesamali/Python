beans=16
def Input1():
    global beans
    while beans>0:
            player1input = int(input("player 1, how many beans would you like to remove?")) 
            if ((player1input > 3) == True) or ((player1input <= 0) == True):
                print("Error: insert only 1,2, or 3 beans") 
                Input1()
            else:
                return player1input
Input1()

def Input2():
    global beans
    while beans>0:
            player2input = int(input("player 2, how many beans would you like to remove?")) 
            if ((player2input > 3) == True) or ((player2input <= 0) == True):
                print("Error: insert only 1,2, or 3 beans") 
                Input2()
            else:
               return player2input
Input2()

def takeBeansOutPlayer1():
    global beans
    player1input = Input1()
    beans = beans - player1input
    if beans > 0:
        print("player 1 loses")
        print("bean value is" +str(beans))
    else:
        return "Game Over"
takeBeansOutPlayer1()

def takeBeansOutPlayer2():
    global beans
    player2input = Input2()
    beans = beans - player2input
    if beans > 0:
        print("player 2 loses")
        print("bean value is" +str(beans))
    else:
        return "Game Over"
takeBeansOutPlayer2()

def beanGame(beans):
    playerbool = True
    print("Main bean value is" +str(beans))
    print("Main bool value is" +str(playerbool))
    while beans>0:
        if playerbool == True:
            takeBeansOutPlayer1()
            playerbool = False
        else:
            takeBeansOutPlayer2()
            playerbool = True
beanGame(beans)
