# Tic Tac Toe Player
import math
import copy

X = 'X'
O = 'O'
EMPTY = None

def initial_state():
    # Returns starting state of the board.
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    # Returns player who has the next turn on a board.
    x_count = 0 
    o_count = 0

    for line in board:
        x_count += line.count('X')
        o_count += line.count('O')

    if x_count == o_count:
        return 'X'
    else:
        return 'O'

def actions(board):
    # Returns set of all possible actions (i, j) available on the board.
    options = set()

    for i, line in enumerate(board):
        for j, cell in enumerate(line):
            if cell == EMPTY:
                options.add((i, j))
    
    return options

def result(board, action):
    # Returns the board that results from making move (i, j) on the board.
    i, j = action

    if board[i][j] != EMPTY:
        raise Exception('Something happened. Try again.')

    next_board = copy.deepcopy(board)
    turn = player(board)

    next_board[i][j] = turn
    return next_board

def winner(board):
    # Returns the winner of the game, if there is one.
    lines = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],

        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],

        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != EMPTY:
            return line[0]

    return None

def terminal(board):
    # Returns True if game is over, False otherwise.
    game_winner = winner(board)
    
    if game_winner != None:
        return True
    
    for line in board:
        for cell in line:
            if cell == EMPTY:
                return False

    return True

def utility(board):
    # Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    game_winner = winner(board)

    if game_winner == 'X':
        return 1
    elif game_winner == 'O':
        return -1
    else:
        return 0

def minimax(board):
    # Returns the optimal action for the current player on the board.
    is_terminal = terminal(board)
    current_player = player(board)

    if is_terminal:
        return None

    if current_player == 'X':
        best_value = -2
        best_action = None

        for action in actions(board):
            new_board = result(board, action)
            value = max_value(new_board)

            if value > best_value:
                best_value = value
                best_action = action

        return best_action
    
    else:
        best_value = 2
        best_action = None

        for action in actions(board):
            new_board = result(board, action)
            value = min_value(new_board)

            if value < best_value:
                best_value = value
                best_action = action

        return best_action

def max_value(board):
    if terminal(board):
        return utility(board)

    value = -2

    for action in actions(board):
        value = max(value, min_value(result(board, action)))

    return value

def min_value(board):
    if terminal(board):
        return utility(board)

    value = 2

    for action in actions(board):
        value = min(value, max_value(result(board, action)))

    return value 