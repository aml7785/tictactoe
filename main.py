from IPython.display import clear_output
import random

def display_board(board):
    board_list = [[board[7],board[8],board[9]],[board[4],board[5],board[6]],[board[1],board[2],board[3]]]
    for i in board_list:
        print(i)


def player_input():
    choice = 'wrong'
    while choice not in ['X', 'O']:
        choice = input('Please choose between X or O')
        if choice not in ['X', 'O']:
            print('Sorry, invalid choice')

    return choice

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    elif board[9] == mark and board[5] == mark and board[1] == mark:
        return True
    elif board[7] == mark and board[4] == mark and board[1] == mark:
        return True
    elif board[8] == mark and board[5] == mark and board[2] == mark:
        return True
    elif board[9] == mark and board[6] == mark and board[3] == mark:
        return True
    else:
        return False


def choose_first():
    random_num = random.randint(1, 10)
    if random_num > 5:
        first_player = player1
        print('Player 1 goes first')
    else:
        first_player = player2
        print('Player 2 goes first')

    return first_player

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in board:
        if i != ' ':
            return True
        else:
            return False

def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Please enter a position between 1 and 9'))

    return position

def replay():
    response = input('Do you want to play again? Enter Y for yes, N for no')
    if response == 'Y':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')
player2 = ''
game_on = 'wrong'
while True:
    # Set the game up here
    def display_board(board):
        board_list = [[board[7], board[8], board[9]], [board[4], board[5], board[6]], [board[1], board[2], board[3]]]
        for i in board_list:
            print(i)


    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1 = player_input()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    # pass
    choose_first()
    while game_on:

        # Player 1 Turn
        position = player_choice(board)
        # space_check(board,position)
        place_marker(board, player1, position)
        display_board(board)
        if win_check(board, player1) == True:
            break

        # Player2's turn.
        position = player_choice(board)
        # space_check(board,position)
        place_marker(board, player2, position)
        display_board(board)
        if win_check(board, player2) == True:
            break

        full_board_check(board)

    if not replay():
        break