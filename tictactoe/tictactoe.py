"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countx=sum(row.count(X) for row in board)
    counto=sum(row.count(O) for row in board)
    return O if countx > counto else X
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                possibleActions.add((i,j))
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action")
    boardcopy = copy.deepcopy(board)
    boardcopy[action[0]][action[1]]=player(board)
    return boardcopy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in [X, O]:
        for i in range(3):
            # Check rows
            if all(cell == player for cell in board[i]):
                return player
            # Check columns
            if all(board[j][i] == player for j in range(3)):
                return player
        # Check diagonals
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return player
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    return all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0

def maxvalue(board):
    v=-math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v=max(v,minvalue(result(board,action)))
    return v
def minvalue(board):
    v=math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v=min(v,maxvalue(result(board,action)))
    return v
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board)==X:
        moves=[]
        for i in actions(board):
            moves.append((minvalue(result(board,i)),i))
        return sorted(moves, key=lambda x: x[0],reverse=True)[0][1]
    elif player(board)==O:
        moves=[]
        for i in actions(board):
            moves.append((maxvalue(result(board,i)),i))
        return sorted(moves, key=lambda x: x[0])[0][1]