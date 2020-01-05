"""
This is a program I wrote a couple years ago. I manually created a tic tac toe bot that doesn't lose. It's pretty bad
code though. Since it works I decided to include it as an example of a bot that was manually created.
"""

# Just a quick reminder that the code is pretty bad syntactically and is unorganized but I might fix that later
from random import randint
from random import choice

# Initializes the board
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
bestmovesx = [0, 2, 4, 6, 8]
bestmoveso = [0, 2, 6, 8]
amount_of_moves = 0


# This will be used to print the current state of the board
def printboard():
    print("Amout of moves: {}".format(amount_of_moves))
    print(board[0] + " | " + board[1] + " | " + board[2] + "\n"
          + "---------" + "\n"
          + board[3] + " | " + board[4] + " | " + board[5] + "\n"
          + "---------" + "\n"
          + board[6] + " | " + board[7] + " | " + board[8] + "\n")


# This used to replace the number with the player's option
def replaceitem(index, character='x'):
    board[index] = character


# Checks if the spot is avalible to be chosen
def checkavailible(index):
    try:
        x = int(board[index])
        return True
    except ValueError:
        return False


# Checks if the entered number is actually an integer or not
def checklocation():
    while True:
        try:
            location = input("What location would you like to go (1, 9),(enter quit to quit): ")
            if location == "quit":
                return -1
            locationfinal = int(location)
            return locationfinal
        except ValueError:
            print("You must enter a integer.")


# Checks if the list is all the same to help check for wins
def checksame(listtouse):
    value = listtouse[0]
    if value != 'x' and value != 'o':
        return False
    for i in listtouse:
        if i != value:
            return False
    return True


def checktwo(char, f1, f2, f3):
    if char == "x":
        ochar = "o"
    else:
        ochar = "x"
    if board[f1] == char and board[f2] == char and board[f3] != ochar:
        return f3
    elif board[f2] == char and board[f3] == char and board[f1] != ochar:
        return f1
    elif board[f1] == char and board[f3] == char and board[f2] != ochar:
        return f2
    return -1


def checkalltwo(thechar):
    if checktwo(thechar, 0, 1, 2) != -1:
        return checktwo(thechar, 0, 1, 2)
    elif checktwo(thechar, 3, 4, 5) != -1:
        return checktwo(thechar, 3, 4, 5)
    elif checktwo(thechar, 6, 7, 8) != -1:
        return checktwo(thechar, 6, 7, 8)
    elif checktwo(thechar, 0, 3, 6) != -1:
        return checktwo(thechar, 0, 3, 6)
    elif checktwo(thechar, 1, 4, 7) != -1:
        return checktwo(thechar, 1, 4, 7)
    elif checktwo(thechar, 2, 5, 8) != -1:
        return checktwo(thechar, 2, 5, 8)
    elif checktwo(thechar, 0, 4, 8) != -1:
        return checktwo(thechar, 0, 4, 8)
    elif checktwo(thechar, 2, 4, 6) != -1:
        return checktwo(thechar, 2, 4, 6)
    return -1


# Checks if there is a tie
def checktie():
    for i in board:
        if i != 'x' and i != 'o':
            return False
    return True


# Checks if there is a win by using the checksame function
def checkwin():
    if (checksame(board[0:3]) or checksame(board[3:6]) or checksame(board[6:])
            or checksame([board[0], board[3], board[6]]) or checksame([board[1], board[4], board[7]]) or checksame(
                [board[2], board[5], board[8]])
            or checksame([board[0], board[4], board[8]]) or checksame([board[2], board[4], board[6]])):
        return True
    else:
        return False


def compbest(index):
    if index == 0 and board[index] == compchar:
        return [2, 6, 8]
    if index == 1 and board[index] == compchar:
        return [0, 2, 4, 7]
    if index == 2 and board[index] == compchar:
        return [0, 8, 6]
    if index == 3 and board[index] == compchar:
        return [0, 6, 4, 5]
    if index == 4 and board[index] == compchar:
        return [0, 2, 6, 8]
    if index == 5 and board[index] == compchar:
        return [2, 8, 4, 3]
    if index == 6 and board[index] == compchar:
        return [0, 8, 2]
    if index == 7 and board[index] == compchar:
        return [4, 1, 6, 8]
    if index == 8 and board[index] == compchar:
        return [2, 6, 0]


def comptesting(index):
    if index == 0 and board[index] == compchar:
        return [1, 2, 3, 6, 4, 8]
    if index == 1 and board[index] == compchar:
        return [0, 2, 4, 7]
    if index == 2 and board[index] == compchar:
        return [0, 1, 5, 8, 4, 6]
    if index == 3 and board[index] == compchar:
        return [0, 6, 4, 5]
    if index == 4 and board[index] == compchar:
        return [0, 1, 2, 3, 5, 6, 7, 8]
    if index == 5 and board[index] == compchar:
        return [2, 8, 4, 3]
    if index == 6 and board[index] == compchar:
        return [3, 0, 7, 8, 4, 2]
    if index == 7 and board[index] == compchar:
        return [4, 1, 6, 8]
    if index == 8 and board[index] == compchar:
        return [2, 4, 7, 5, 6, 0]


print("Hello and welcome to tic tac toe!" + '\n'
      + "Author: Will Ryan")

lastcompmove = -1

while True:
    character = input("Would you like to be x or o (x,o): ")
    if character == 'x' or character == 'o':
        break
if character == 'x':
    compchar = 'o'
else:
    compchar = 'x'

if character == 'o':
    while True:
        compindex = choice(bestmovesx)
        if checkavailible(compindex):
            lastcompmove = compindex
            break
    replaceitem(compindex, compchar)

printboard()

while True:
    location = checklocation()
    if location == -1:
        print("Goodbye")
        break
    while True:
        if checkavailible(location - 1):
            replaceitem(index=location - 1, character=character)
            if amount_of_moves == 0:
                first_move = location - 1
            if amount_of_moves == 1:
                second_move = location - 1
            break
        else:
            print("Sorry that location is unavailible")
            location = checklocation()
    if checkwin():
        print("Congratulations you won.")
        printboard()
        break
    if checktie():
        print("It was a Tie")
        printboard()
        break
    if lastcompmove == -1:
        if checkavailible(4):
            lastcompmove = 4
            replaceitem(4, compchar)
        else:
            while True:
                compindex = choice(bestmoveso)
                if checkavailible(compindex):
                    lastcompmove = compindex
                    break
            replaceitem(compindex, compchar)
    else:
        checks = checkalltwo(compchar)
        checks2 = checkalltwo(character)
        if checks != -1:
            replaceitem(checks, compchar)
            lastcompmove = checks
        elif checks2 != -1:
            replaceitem(checks2, compchar)
            lastcompmove = checks2
        else:
            if (character == 'x' and amount_of_moves == 1 and (
                    (first_move == 0 and second_move == 8) or (first_move == 8 and second_move == 0))):
                replaceitem(7, compchar)
                lastcompmove = 7
            elif (character == 'x' and amount_of_moves == 1 and (
                    (first_move == 2 and second_move == 6) or (first_move == 6 and second_move == 2))):
                replaceitem(1, compchar)
                lastcompmove = 1
            elif character == 'x' and amount_of_moves == 1 and (first_move == 0 and second_move == 5):
                replaceitem(2, compchar)
                lastcompmove = 2
            elif character == 'x' and amount_of_moves == 1 and (first_move == 2 and second_move == 3):
                replaceitem(0, compchar)
                lastcompmove = 0
            elif character == 'x' and amount_of_moves == 1 and (first_move == 6 and second_move == 5):
                replaceitem(8, compchar)
                lastcompmove = 8
            elif character == 'x' and amount_of_moves == 1 and (first_move == 8 and second_move == 3):
                replaceitem(6, compchar)
                lastcompmove = 6
            elif character == 'o' and amount_of_moves == 0 and (lastcompmove == 0) and first_move == 4:
                replaceitem(8, compchar)
                lastcompmove = 8
            elif character == 'o' and amount_of_moves == 0 and (lastcompmove == 2) and first_move == 4:
                replaceitem(6, compchar)
                lastcompmove = 6
            elif character == 'o' and amount_of_moves == 0 and (lastcompmove == 6) and first_move == 4:
                replaceitem(2, compchar)
                lastcompmove = 2
            elif character == 'o' and amount_of_moves == 0 and (lastcompmove == 8) and first_move == 4:
                replaceitem(0, compchar)
                lastcompmove = 0
            else:
                arrop = compbest(lastcompmove)
                avail = False
                availop = []
                for i in arrop:
                    if checkavailible(i):
                        item = board[i]
                        replaceitem(i, compchar)
                        if checkalltwo(compchar) != -1:
                            availop.append(i)
                            avail = True
                        replaceitem(i, item)
                if avail:
                    compindex = choice(availop)
                    lastcompmove = compindex
                    replaceitem(compindex, compchar)
                else:
                    arop = comptesting(lastcompmove)
                    avil = False
                    avilop = []
                    for i in arop:
                        if checkavailible(i):
                            item = board[i]
                            replaceitem(i, compchar)
                            if checkalltwo(compchar) != -1:
                                avilop.append(i)
                                avil = True
                            replaceitem(i, item)
                    if avil:
                        compindex = choice(avilop)
                        lastcompmove = compindex
                        replaceitem(compindex, compchar)
                    else:
                        while True:
                            compindex = randint(0, 8)
                            if checkavailible(compindex):
                                lastcompmove = compindex
                                break
                        replaceitem(compindex, compchar)
    if checkwin():
        print("The Computer won.")
        printboard()
        break
    if checktie():
        print("It was a Tie")
        printboard()
        break

    amount_of_moves += 1

    printboard()
