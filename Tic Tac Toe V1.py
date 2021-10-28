from os import system, name

playerX = False
playerO = False
gameEnded = False
winner = ''


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Total ways of winning are 8 for X or O. 3 vert, 3 horizontal, 2 diagonal
def winnerDecidertron(board):
    global playerX
    global playerO
    global gameEnded
    global winner

    if board[indexesOfInterest[1]] == 'X' and board[indexesOfInterest[2]] == 'X' and board[indexesOfInterest[3]] == 'X':
        gameEnded = True
        playerX = True
    elif board[indexesOfInterest[4]] == 'X' and board[indexesOfInterest[5]] == 'X' and board[indexesOfInterest[6]] == 'X':
        gameEnded = True
        playerX = True
    elif board[indexesOfInterest[7]] == 'X' and board[indexesOfInterest[8]] == 'X' and board[indexesOfInterest[9]] == 'X':
        gameEnded = True
        playerX = True
    elif board[indexesOfInterest[1]] == 'X' and board[indexesOfInterest[5]] == 'X' and board[indexesOfInterest[9]] == 'X':
        gameEnded = True
        playerX = True
    elif board[indexesOfInterest[3]] == 'X' and board[indexesOfInterest[5]] == 'X' and board[indexesOfInterest[7]] == 'X':
        gameEnded = True
        playerX = True
    elif board[indexesOfInterest[1]] == 'X' and board[indexesOfInterest[4]] == 'X' and board[indexesOfInterest[7]] == 'X':
        gameEnded = True
        playerX = True
    elif board[indexesOfInterest[2]] == 'X' and board[indexesOfInterest[5]] == 'X' and board[indexesOfInterest[8]] == 'X':
        gameEnded = True
        playerX = True
    elif board[indexesOfInterest[3]] == 'X' and board[indexesOfInterest[6]] == 'X' and board[indexesOfInterest[9]] == 'X':
        gameEnded = True
        playerX = True

    if board[indexesOfInterest[1]] == 'O' and board[indexesOfInterest[2]] == 'O' and board[indexesOfInterest[3]] == 'O':
        gameEnded = True
        playerO = True
    elif board[indexesOfInterest[4]] == 'O' and board[indexesOfInterest[5]] == 'O' and board[indexesOfInterest[6]] == 'O':
        gameEnded = True
        playerO = True
    elif board[indexesOfInterest[7]] == 'O' and board[indexesOfInterest[8]] == 'O' and board[indexesOfInterest[9]] == 'O':
        gameEnded = True
        playerO = True
    elif board[indexesOfInterest[1]] == 'O' and board[indexesOfInterest[5]] == 'O' and board[indexesOfInterest[9]] == 'O':
        gameEnded = True
        playerO = True
    elif board[indexesOfInterest[3]] == 'O' and board[indexesOfInterest[5]] == 'O' and board[indexesOfInterest[7]] == 'O':
        gameEnded = True
        playerO = True
    elif board[indexesOfInterest[1]] == 'O' and board[indexesOfInterest[4]] == 'O' and board[indexesOfInterest[7]] == 'O':
        gameEnded = True
        playerO = True
    elif board[indexesOfInterest[2]] == 'O' and board[indexesOfInterest[5]] == 'O' and board[indexesOfInterest[8]] == 'O':
        gameEnded = True
        playerO = True
    elif board[indexesOfInterest[3]] == 'O' and board[indexesOfInterest[6]] == 'O' and board[indexesOfInterest[9]] == 'O':
        gameEnded = True
        playerO = True

    if playerX:
        winner = 'Player X won the Game. Congrats!!'
    elif playerO:
        winner = 'Player O won the Game. Congrats!!'

    return gameEnded, winner


currentState = """   |   |   \n   |   |   \n   |   |   """
indexesOfInterest = {1: 1, 2: 5, 3: 9, 4: 13, 5: 17, 6: 21, 7: 25, 8: 29, 9: 33}
clear()
print("Welcome to the Tic-Tac-Toe game.")
counter = 0

while True:
    try:
        if counter % 2 == 0:
            print('Player X Turn')
            while True:
                print(currentState)
                target = indexesOfInterest[int(input("Enter the target place(1-9) > "))]
                if currentState[target].isspace():
                    currentState = currentState[:target] + 'X' + currentState[target + 1:]
                    break
                else:
                    clear()
                    print('Please Enter an empty target space.')
                    continue
        else:
            print('Player O Turn')
            while True:
                print(currentState)
                target = indexesOfInterest[int(input("Enter the target place(1-9) > "))]
                if currentState[target].isspace():
                    currentState = currentState[:target] + 'O' + currentState[target + 1:]
                    break
                else:
                    clear()
                    print('Please Enter an empty target space.')
                    continue
        counter += 1

        result, message = winnerDecidertron(currentState)

        if counter == 9 or result:
            if result:
                print(message)
            else:
                print("The game ended in a draw.")
            break
        elif counter != 9 and result is False:
            clear()
            continue

    except (ValueError, KeyError) as error:
        clear()
        print("Please Behave!")
        continue
