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
    conutx=0
    conuto=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                conutx+=1
            elif board[i][j]==O:
                conuto+=1
    if conutx>conuto:
        return O
    else:
        return X


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
    row,coloumn = action
    boardcopy = copy.deepcopy(board)
    boardcopy[row][coloumn]=player(board)
    return boardcopy

def rowcheck(board,player):
    for i in range(3):
        if board[i][0]==player and board[i][1]==player and board[i][2]==player:
            return True
    return False
def coloumncheck(board,player):
    for i in range(3):
        if board[0][i]==player and board[1][i]==player and board[2][i]==player:
            return True
    return False
def diagonalcheck(board,player):
    n=0 #count for diagonal
    for i in range(3):
        for j in range(3):
            if i==j and board[i][j]==player:
                n+=1
    if n==3:
        return True
    else :
        return False
def diagonalcheck2(board,player):
    n=0 #count for diagonal
    for i in range(3):
        for j in range(3):
            if (3-i-1)==j and board[i][j]==player:
                n+=1
    if n==3:
        return True
    else :
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if rowcheck(board,X) or coloumncheck(board,X) or diagonalcheck(board,X) or diagonalcheck2(board,X):
        return X
    elif rowcheck(board,O) or coloumncheck(board,O) or diagonalcheck(board,O) or diagonalcheck2(board,O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)==X or winner(board)==O:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                return False
    return True

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