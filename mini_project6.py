# Mini-project 6 for Principles of Computing class, by k., 07/25/2014
# Tic-Tac-Toe (based on Minimax method)
# http://www.codeskulptor.org/#poc_tttmm_template.py


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
Minimax Tic-Tac-Toe Player
'''

#import poc_ttt_gui
#import poc_ttt_provided as provided

# set timeout, as minimax can take a long time
#import codeskulptor
#codeskulptor.set_timeout(60)

# scoring values, DO NOT MODIFY!, for grader add provided.
SCORES = {PLAYERX: 1,
          DRAW: 0,
          PLAYERO: -1}

def mm_move(board, player):
    '''
    make a move on the board,
    
    returns a tuple with two elements; the first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col)
    '''
    # base case, the game is effectively over
    if board.check_win() is not None:
        return SCORES[board.check_win()], (-1, -1)

    # recursion(s)
    # worst possible initial values
    result = (-1, (-1, -1))
    # depth first search along the tree
    for move in board.get_empty_squares():
        copied_board = board.clone()
        copied_board.move(move[0], move[1], player)
        score, _ = mm_move(copied_board, switch_player(player))    # for grader add provided.
        # best possible choice found already
        if score * SCORES[player] == 1:
            return score, move
        # update the initial values
        elif score * SCORES[player] > result[0]:
            result = (score, move)
        elif result[0] == -1:
            result = (result[0], move)
            
    return result[0] * SCORES[player], result[1]

            
def move_wrapper(board, player, trials):
    '''
    wrapper function to allow the use of the same infrastructure that was used
    for Tic-Tac-Toe (Monte Carlo method)
    '''
    move = mm_move(board, player)
    assert move[1] != (-1, -1), 'returned illegal move (-1, -1)'
    return move[1]

# test game with the console or the GUI; uncomment whichever you prefer
# both should be commented out when you submit for testing to save time

#play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
