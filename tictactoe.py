import random

#board
board = ['-','-','-',
        '-','-','-',
        '-','-','-',]

#display function
def display():
    print('Tic-Tac Toe')
    print('----------')
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('----------')

def play():
    turn()

#users turn 
def turn():
    display()
    x = False
    if checkfull()==True:
        print('You have tied.')
        playagain()
    elif checkcomp()==True:
        x = True
        playagain()
    else:
        while x == False:
            pos = int(input("Enter in a position(1-9): "))
            if pos < 1 or pos > 9:
                x = False
            else:
                x = True
                pos = pos -1
                if board[pos] == 'X':
                    print('You already have this position.')
                    x = False
                elif board[pos] == 'O':
                    print('The computer owns this position.')
                    x = False
                else:
                    board[pos] = 'X'
                    try:
                        oppose()
                    except RecursionError:
                        display()
                        print('You have tied!')
                        playagain()


#random pos for computer
def randpos():
    global cPos
    cPos = random.randrange(9)

#computers turn
def oppose():
    randpos()
    if checkfull()==True:
        print('You have tied.')
        playagain()
    elif checkuser()==True:
        print()
        playagain()
    else:
        if board[cPos] == 'X' or board[cPos] == 'O':
            oppose()
        else:
            board[cPos] = 'O'
            turn()

#check if user has won
def checkuser():
    if board[0] =='X' and board[3] =='X' and board[6] =='X':
        display()
        print('You won the game.')
        return True
    if board[1] =='X' and board[4] =='X' and board[7] =='X':
        display()
        print('You won the game.')
        return True
    if board[2] =='X' and board[5] =='X' and board[8] =='X':
        display()
        print('You won the game.')
        return True
    if board[0] =='X' and board[1] =='X' and board[2] =='X':
        display()
        print('You won the game.')
        return True
    if board[3] =='X' and board[4] =='X' and board[5] =='X':
        display()
        print('You won the game.')
        return True
    if board[6] =='X' and board[7] =='X' and board[8] =='X':
        display()
        print('You won the game.')
        return True
    if board[0] =='X' and board[4] =='X' and board[8] =='X':
        display()
        print('You won the game.')
        return True
    if board[2] =='X' and board[4] =='X' and board[6] =='X':
        display()
        print('You won the game.')
        return True
    else:
        return False

#check if computer won
def checkcomp():
    if board[0] =='O' and board[3] =='O' and board[6] =='O':
        print('The computer has one the game.')
        return True
    if board[1] =='O' and board[4] =='O' and board[7] =='O':
        print('The computer has one the game.')
        return True
    if board[2] =='O' and board[5] =='O' and board[8] =='O':
        print('The computer has one the game.')
        return True
    if board[0] =='O' and board[1] =='O' and board[2] =='O':
        print('The computer has one the game.')
        return True
    if board[3] =='O' and board[4] =='O' and board[5] =='O':
        print('The computer has one the game.')
        return True
    if board[6] =='O' and board[7] =='O' and board[8] =='O':
        print('The computer has one the game.')
        return True
    if board[0] =='O' and board[4] =='O' and board[8] =='O':
        print('The computer has one the game.')
        return True
    if board[2] =='O' and board[4] =='O' and board[6] =='O':
        print('The computer has one the game.')
        return True
    else:
        return False

#resets board

def reset():
    for i in range(len(board)):
        board[i] = '-'

#play again
def playagain():
    x = False
    while x == False:
        play = input('Do you want to play again? Y/N ').upper()
        if play == 'Y' or play == 'N':
            if play == 'Y':
                x = True
                reset()
                turn()
            if play == 'N':
                print('Thank you for playing!')
                x = True
        else:
            x = False

#check if the board is full
def checkfull():
    count = 0
    for i in range(len(board)-1):
        if board[i] == 'X' or board[i] == 'O':
            count += 1
        if count == 9:
            return True
        else:
            return False


    
#calls the function to start the game
play()



