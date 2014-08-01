# Homework 7 for Principles of Computing class, by k., 08/01/2014

# class Puzzle from program template at http://www.codeskulptor.org/#poc_fifteen_template.py

'''
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
'''

#import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction


# start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))


# Question 1

question1 = Puzzle(4, 4)
print 'Prep for Question 1 follows...\n', question1
question1.update_puzzle('drdr')
print 'Configuration after move \'drdr\':\n', question1

        
# Question 2

question2 = Puzzle(4, 4)
question2.update_puzzle('ddrdrudlulurrrlldluurrrdllldr')
print '\nPrep for Question 2 follows...\n', question2
question2.update_puzzle('urullddruld')
print 'Configuration after move \'urullddruld\':\n', question2


# Question 3

question3 = Puzzle(2, 2)
print '\nPrep for Question 3 follows...\n', question3
question3.update_puzzle('rdlu')
print 'First move:\n', question3
question3.update_puzzle('rdlu')
print 'Second move:\n', question3
question3.update_puzzle('rdlu')
print 'Configuration after third move:\n', question3


# Question 4

question4 = Puzzle(2, 2, [[0, 2], [3, 1]])
print '\nPrep for Question 4 follows...\n', question4
question4.update_puzzle('rdlu')
print 'Configuration after move \'rdlu\':\n', question4


# Question 5

question5 = Puzzle(2, 2, [[0, 3], [1, 2]])
print '\nPrep for Question 5 follows...\n', question5
question5.update_puzzle('drul')
print 'Configuration after move \'drul\':\n', question5


# Question 8

question8 = Puzzle(4, 4, [[4, 13, 1, 3], [5, 10, 2, 7], [8, 12, 6, 11], [9, 0, 14, 16]])
print '\nPrep for Question 8 follows...\n', question8
question8.update_puzzle('uuu')
print 'Configuration after move \'uuu\':\n', question8
question8.update_puzzle('lddru')
print 'Configuration after move \'lddru\':\n', question8
question8.update_puzzle('lddruld')
print 'Configuration after move \'lddruld\':\n', question8


# Question 9

question9 = Puzzle(3, 2, [[1, 2], [0, 4], [3, 5]])
print '\nPrep for Question 9 follows...\n', question9
question9.update_puzzle('ruldrdlurdluurddlur')
print 'Configuration after move \'ruldrdlurdluurddlur\':\n', question9


# Question 10

question10 = Puzzle(2, 3, [[3, 4, 1], [0, 2, 5]])
print '\nPrep for Question 10 follows...\n', question10
question10.update_puzzle('urdlurrdluldrruld')
print 'Configuration after move \'urdlurrdluldrruld\':\n', question10
