import sys

COMPUTER = 1
HUMAN = 2

SIDE = 3  # Length of the board

# Computer will move with 'O'
# and human with 'X'
COMPUTERMOVE = 'O'
HUMANMOVE = 'X'


# A function to show the current board status
def showBoard(board):
    print("\t\t\t", board[0][0], "|", board[0][1], "|", board[0][2])
    print("\t\t\t-----------")
    print("\t\t\t", board[1][0], "|", board[1][1], "|", board[1][2])
    print("\t\t\t-----------")
    print("\t\t\t", board[2][0], "|", board[2][1], "|", board[2][2], "\n")


# A function to show the instructions
def showInstructions():
    print("\nChoose a cell numbered from 1 to 9 as below and play\n")
    print("\t\t\t 1 | 2 | 3 ")
    print("\t\t\t-----------")
    print("\t\t\t 4 | 5 | 6 ")
    print("\t\t\t-----------")
    print("\t\t\t 7 | 8 | 9 \n")


# A function to initialise the game
def initialise(board):
    # Initially the board is empty
    for i in range(SIDE):
        for j in range(SIDE):
            board[i][j] = ' '


# A function to declare the winner of the game
def declareWinner(whoseTurn):
    if whoseTurn == COMPUTER:
        print("COMPUTER has won")
    else:
        print("HUMAN has won")


# A function that returns true if any of the row
# is crossed with the same player's move
def rowCrossed(board):
    for i in range(SIDE):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
    return False


# A function that returns true if any of the column
# is crossed with the same player's move
def columnCrossed(board):
    for i in range(SIDE):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    return False


# A function that returns true if any of the diagonal
# is crossed with the same player's move
def diagonalCrossed(board):
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


# A function that returns true if the game is over
# else it returns false
def gameOver(board):
    return rowCrossed(board) or columnCrossed(board) or diagonalCrossed(board)


# Function to calculate best score
def minimax(board, depth, isAI):
    score = 0
    bestScore = 0

    if gameOver(board):
        if isAI:
            return -1
        else:
            return +1
    else:
        if depth < 9:
            if isAI:
                bestScore = -999
                for i in range(SIDE):
                    for j in range(SIDE):
                        if board[i][j] == ' ':
                            board[i][j] = COMPUTERMOVE
                            score = minimax(board, depth + 1, False)
                            board[i][j] = ' '
                            if score > bestScore:
                                bestScore = score
                return bestScore
            else:
                bestScore = 999
                for i in range(SIDE):
                    for j in range(SIDE):
                        if board[i][j] == ' ':
                            board[i][j] = HUMANMOVE
                            score = minimax(board, depth + 1, True)
                            board[i][j] = ' '
                            if score < bestScore:
                                bestScore = score
                return bestScore
        else:
            return 0


# Function to calculate best move
def bestMove(board, moveIndex):
    x = -1
    y = -1
    score = 0
    bestScore = -999
    for i in range(SIDE):
        for j in range(SIDE):
            if board[i][j] == ' ':
                board[i][j] = COMPUTERMOVE
                score = minimax(board, moveIndex + 1, False)
                board[i][j] = ' '
                if score > bestScore:
                    bestScore = score
                    x = i
                    y = j
    return x * 3 + y


# A function to play Tic-Tac-Toe
def playTicTacToe(whoseTurn):
    board = [[' ' for _ in range(SIDE)] for _ in range(SIDE)]
    moveIndex = 0
    x = 0
    y = 0

    initialise(board)
    showInstructions()

    # Keep playing till the game is over or it is a draw
    while not gameOver(board) and moveIndex != SIDE * SIDE:
        if whoseTurn == COMPUTER:
            n = bestMove(board, moveIndex)
            x = n // SIDE
            y = n % SIDE
            board[x][y] = COMPUTERMOVE
            print(f"COMPUTER has put a {COMPUTERMOVE} in cell {n+1}\n")
            showBoard(board)
            moveIndex += 1
            whoseTurn = HUMAN

        elif whoseTurn == HUMAN:
            available_positions = []
            print("You can insert in the following positions: ", end='')
            for i in range(SIDE):
                for j in range(SIDE):
                    if board[i][j] == ' ':
                        available_positions.append(i * 3 + j + 1)
            print(*available_positions)
            print("\nEnter the position: ", end='')
            n = int(input()) - 1
            x = n // SIDE
            y = n % SIDE
            if board[x][y] == ' ' and 0 <= n < 9:
                board[x][y] = HUMANMOVE
                print(f"\nHUMAN has put a {HUMANMOVE} in cell {n+1}\n")
                showBoard(board)
                moveIndex += 1
                whoseTurn = COMPUTER
            elif 0 <= n < 9:
                print("\nPosition is occupied, select any one place from the available places\n")
            else:
                print("Invalid position")

    # If the game has drawn
    if not gameOver(board) and moveIndex == SIDE * SIDE:
        print("It's a draw")
    else:
        # Toggling the user to declare the actual winner
        if whoseTurn == COMPUTER:
            whoseTurn = HUMAN
        else:
            whoseTurn = COMPUTER

        declareWinner(whoseTurn)


if __name__ == '__main__':
    print("\n-------------------------------------------------------------------\n")
    print("\t\t\t Tic-Tac-Toe\n")
    print("\n-------------------------------------------------------------------\n")
    cont = 'y'
    while cont == 'y':
        choice = input("Do you want to start first? (y/n): ")
        if choice == 'n':
            playTicTacToe(COMPUTER)
        elif choice == 'y':
            playTicTacToe(HUMAN)
        else:
            print("Invalid choice")

        cont = input("\nDo you want to continue? (y/n): ")
    print("Thank you for playing Tic-Tac-Toe!")
