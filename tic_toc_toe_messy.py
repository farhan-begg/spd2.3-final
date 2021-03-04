# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

def draw_board(board):
    ''' This function prints out board'''
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

def input_player_letter():
    ''' lets player input and returns list with player’s and computers letter'''
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']

def who_goes_first():
   '''randomly selects player or computer to go first'''
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def play_again():
    ''' ask player to play again'''
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    ''' Given a board and a player’s letter, this function returns True if that player has won. '''
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle    
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def get_board_copy(board):
    ''' Make a duplicate of the board list and return it the duplicate. '''
    dupe_board= []
    for i in board:
        dupe_board.append(i)
    return dupe_board

def is_space_free(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def get_player_move(board):
    ''' Let the player type in their move.'''
    move = ' ' # TODO: W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def choose_random_move_from_list(board, movesList):
    '''Returns a valid move from the passed list on the passed board.
         Returns None if there is no valid move. '''
    possibleMoves = []
    for i in movesList:
        if is_space_free(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0: # TODO: How would you write this pythanically? (You can google for it!)
        return random.choice(possibleMoves)
    else: # TODO: is this 'else' necessary?
        return None

def get_computer_move(board, computerLetter): # TODO: W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computerLetter, i)
            if is_winner(copy, computerLetter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, playerLetter, i)
            if is_winner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None: # TODO: Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

# TODO: The following mega code block is a huge hairy monster. Break it down 
# into smaller methods. Use TODO s and the comment above each section as a guide 
# for refactoring.

while True:
    # Reset the board
    theBoard = [' '] * 10 # TODO: Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
    playerLetter, computerLetter = input_player_letter()
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True # TODO: Study how this variable is used. Does it ring a bell? (which refactoring method?) 
                         #       See whether you can get rid of this 'flag' variable. If so, remove it.

    while gameIsPlaying: # TODO: Usually (not always), loops (or their content) are good candidates to be extracted into their own function.
                         #       Use a meaningful name for the function you choose.
        if turn == 'player':
            # Player’s turn.
            draw_board(theBoard)
            move = get_player_move(theBoard)
            make_move(theBoard, playerLetter, move)

            if is_winner(theBoard, playerLetter):
                draw_board(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:  # TODO: is this 'else' necessary?
                if is_board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie!')
                    break
                else:  # TODO: Is this 'else' necessary?
                    turn = 'computer'

        else:
            # Computer’s turn.
            move = get_computer_move(theBoard, computerLetter)
            make_move(theBoard, computerLetter, move)

            if is_winner(theBoard, computerLetter):
                draw_board(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:     # TODO: is this 'else' necessary?
                if is_board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie!')
                    break
                else: # TODO: Is this 'else' necessary?
                    turn = 'player'

    if not play_again():
        break