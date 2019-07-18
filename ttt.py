turnNum = 0
def inputPlayerLetter():

   letter = ''
   while not (letter == 'X' or letter == 'O'):
       print('Do you want to be X or O?')
       letter = input().upper()
   if letter == 'X':
       return ['X', 'O']
   else:
       return ['O', 'X']

grid = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
drawBoard(grid)

# gameOver = False

def isWinner(board, letter):
    
    if (board[7] == letter and board[8] == letter and board[9] == letter):
        print(letter + " wins!")
        gameOver = True
        return gameOver
    
    
    if (board[4] == letter and board[5] == letter and board[6] == letter):
        print(letter + "wins!")
        gameOver = True
        return gameOver
    
    
    if (board[1] == letter and board[2] == letter and board[3] == letter):
        print(letter + "wins!")
        gameOver = True
        return gameOver
    
    
    if (board[7] == letter and board[4] == letter and board[1] == letter):
        print(letter + "wins!")
        gameOver = True
        return gameOver
    
    
    if (board[8] == letter and board[5] == letter and board[2] == letter):
        print(letter + "wins!")
        gameOver = True
        return gameOver
    
    
    if (board[9] == letter and board[6] == letter and board[3] == letter):
        print(letter + "wins!")
        gameOver = True
        return gameOver
    
    
    if(board[7] == letter and board[5] == letter and board[3] == letter):
        print(letter + "wins!")
        gameOver = True
        return gameOver
    
    
    if (board[9] == letter and board[5] == letter and board[1] == letter):
        print(letter+"wins!")
        gameOver = True
        return gameOver
    
    
# turnNum = 1

while turnNum < 9:
    answer=input("Player 1, What box number do you want?")
    grid[int(answer)] = "X"
    turnNum = turnNum + 1
    drawBoard(grid)
    gameCheck = isWinner(grid, "X")
    
    if gameCheck == True:
        again=str(input("Play again?"))
        if again == "no":
            play = False
            break
        else:
            grid = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
    answer=input("Player 2, What box number do you want?")
    grid[int(answer)] = "O"
    drawBoard(grid)
    gameCheck = isWinner(grid, "O")
    
    if gameCheck == True:
        again=str(input("Play again?"))
        if again == "no":
            play = False
            break
        else:
            grid = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        

    # turnNum = turnNum+1


    
    
    
    
    
    
    
    
# drawBoard(grid)
