# Mini-project 2 for Principles of Computing class, by k., 06/27/2014
# Tic-Tac-Toe (simulator based on Monte Carlo method)
# http://www.codeskulptor.org/#poc_ttt_template.py


# TTTBoard Class described and provided at: 
# https://class.coursera.org/principlescomputing-001/wiki/TTTBoard
# http://www.codeskulptor.org/#poc_ttt_provided.py

'''
TTTBoard Class Information
'''

# Constants
EMPTY = 1
PLAYERX = 2
PLAYERO = 3 
DRAW = 4

# Map player constants to letters for printing
STRMAP = {EMPTY: " ",
          PLAYERX: "X",
          PLAYERO: "O"}

class TTTBoard:
    """
    Class to represent a Tic-Tac-Toe board.
    """

    def __init__(self, dim, reverse = False, board = None):
        self._dim = dim
        self._reverse = reverse
        if board == None:
            # Create empty board
            self._board = [[EMPTY for dummycol in range(dim)] 
                           for dummyrow in range(dim)]
        else:
            # Copy board grid
            self._board = [[board[row][col] for col in range(dim)] 
                           for row in range(dim)]
            
    def __str__(self):
        """
        Human readable representation of the board.
        """
        rep = ""
        for row in range(self._dim):
            for col in range(self._dim):
                rep += STRMAP[self._board[row][col]]
                if col == self._dim - 1:
                    rep += "\n"
                else:
                    rep += " | "
            if row != self._dim - 1:
                rep += "-" * (4 * self._dim - 3)
                rep += "\n"
        return rep

    def get_dim(self):
        """
        Return the dimension of the board.
        """
        return self._dim
    
    def square(self, row, col):
        """
        Return the status (EMPTY, PLAYERX, PLAYERO) of the square at
        position (row, col).
        """
        return self._board[row][col]

    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares
        """
        empty = []
        for row in range(self._dim):
            for col in range(self._dim):
                if self._board[row][col] == EMPTY:
                    empty.append((row, col))
        return empty

    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).
        Does nothing if board square is not empty.
        """
        if self._board[row][col] == EMPTY:
            self._board[row][col] = player

    def check_win(self):
        """
        If someone has won, return player.
        If game is a draw, return DRAW.
        If game is in progress, return None.
        """
        lines = []

        # rows
        lines.extend(self._board)

        # cols
        cols = [[self._board[rowidx][colidx] for rowidx in range(self._dim)]
                for colidx in range(self._dim)]
        lines.extend(cols)

        # diags
        diag1 = [self._board[idx][idx] for idx in range(self._dim)]
        diag2 = [self._board[idx][self._dim - idx -1] 
                 for idx in range(self._dim)]
        lines.append(diag1)
        lines.append(diag2)

        # check all lines
        for line in lines:
            if len(set(line)) == 1 and line[0] != EMPTY:
                if self._reverse:
                    return switch_player(line[0])
                else:
                    return line[0]

        # no winner, check for draw
        if len(self.get_empty_squares()) == 0:
            return DRAW

        # game is still in progress
        return None
            
    def clone(self):
        """
        Return a copy of the board.
        """
        return TTTBoard(self._dim, self._reverse, self._board)


def switch_player(player):
    """
    Convenience function to switch players.
    
    Returns other player.
    """
    if player == PLAYERX:
        return PLAYERO
    else:
        return PLAYERX

def play_game(mc_move_function, ntrials, reverse = False):
    """
    Function to play a game with two MC players.
    """
    # Setup game
    board = TTTBoard(3, reverse)
    curplayer = PLAYERX
    winner = None
    
    # Run game
    while winner == None:
        # Move
        row, col = mc_move_function(board, curplayer, ntrials)
        board.move(row, col, curplayer)

        # Update state
        winner = board.check_win()
        curplayer = switch_player(curplayer)

        # Display board
        print board
        print
        
    # Print winner
    if winner == PLAYERX:
        print "X wins!"
    elif winner == PLAYERO:
        print "O wins!"
    elif winner == DRAW:
        print "Tie!"
    else:
        print "Error: unknown winner"



'''
Monte Carlo Tic-Tac-Toe Player
'''

import random
#import poc_ttt_gui
#import poc_ttt_provided as provided

# constants for Monte Carlo simulator
# change as desired
NTRIALS = 1    # number of trials to run
MCMATCH = 1.0  # score for squares played by the machine player
MCOTHER = 1.0  # score for squares played by the other player
    
def mc_trial(board, player):
    '''
    takes a current board and the next player to move,
    play a game starting with the given player by making random moves, alternating between players;
    modified board will contain the state of the game, does not return anything
    '''
    currently_empty_squares = board.get_empty_squares()

    while currently_empty_squares:
        square = random.choice(currently_empty_squares)
        # current player plays the square
        board.move(square[0], square[1], player)
        currently_empty_squares.remove(square)
        # done if the result is a winner or draw game (if returns anything but None)
        if board.check_win(): 
            break
        player = switch_player(player) # add 'provided.' for grader submission

def mc_update_scores(scores, board, player):
    '''
    a grid of scores (a list of lists), score the completed board and update the scores grid,
    the function updates the scores grid directly, it does not return anything
    '''
    winner = board.check_win()

    # looping through the grid and assigning scores for win/lose
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            player = board.square(row, col)
            if player == PLAYERX:
                if winner == PLAYERX:
                    scores[row][col] += MCMATCH
                elif winner == PLAYERO:
                    scores[row][col] += -MCOTHER
            elif player == PLAYERO:
                if winner == PLAYERX:
                    scores[row][col] += -MCOTHER
                elif winner == PLAYERO:
                    scores[row][col] += MCMATCH
            else:
                # the rest is 0 value, don't care as it has no effect on score
                pass

def get_best_move(board, scores):
    '''
    function find all of the empty squares with the maximum score and
    randomly return one of them as a (row, column) tuple;
    board that has no empty squares results in error message
    '''
    maximum_score = []
    maximum = float('-inf')
    empty_squares = board.get_empty_squares()
    
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if scores[row][col] > maximum and (row, col) in empty_squares:
                maximum = scores[row][col]
                maximum_score = [(row, col)]
            elif scores[row][col] == maximum and (row, col) in empty_squares:
                maximum_score.append((row, col))

    return random.choice(maximum_score)
        
def mc_move(board, player, trials):
    '''
    return a move for the machine player in the form of a (row, column) tuple
    '''
    # creates initial score board with every values sets to 0
    initial_scores = [[0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]

    for dummy_trial in range(trials):
        cloned = board.clone()
        mc_trial(cloned, player)
        mc_update_scores(initial_scores, cloned, player)
        
    return get_best_move(board, initial_scores)


# test game with the console or the GUI,
# uncomment whichever you prefer,
# both should be commented out when you submit for testing to save time

play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
