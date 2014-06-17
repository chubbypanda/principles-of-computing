# Mini-project 0 for Principles of Computing class, by k., 06/13/2014
# clone of 2048 game; GUI is provided in codeskulptor (obscure Python interpretter for the class) at:
# http://www.codeskulptor.org/#poc_2048_template.py

def merge(line):
    '''
    helper function that merges a single row or column in 2048
    '''
    original_lenght = len(line)
    empty_space = 0

    # slide all tiles towards the front by removing empty spaces (zero values)
    while empty_space in line:
        line.remove(empty_space)

    for tile in xrange(len(line)):
        # arrived at the end of list
        if tile + 1 > len(line) - 1:
            break
        # merge pair of eligible neighbors
        if line[tile] == line[tile + 1]:
            line[tile] *= 2
            del line[tile + 1]
            line.insert(tile + 1, empty_space)

    # slide all the tiles towards the front and fill the rest with zeros
    while empty_space in line:
        line.remove(empty_space)
    while len(line) != original_lenght:
        line.append(empty_space)

    return line

# few simple tests
##print merge([2, 0, 2, 4])
##print merge([0, 0, 2, 2])
##print merge([2, 2, 0, 0])
##print merge([2, 2, 2, 2])
##print merge([4, 4, 4, 4])
##print merge([8, 16, 16, 8])
##print merge([0, 0, 0, 0])


import random

# directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

class TwentyFortyEight(object):
    '''
    class to run the game logic
    '''
    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        # reset the grid at the beginning of each game
        self.reset()

    def reset(self):
        '''
        reset the game so the grid is empty
        '''
        # 'dummy_' string is to satisfy pylint rule about unused variables
        self.cells = [[0 for dummy_col in range(self.grid_width)] for dummy_row in range(self.grid_height)]

    def __str__(self):
        '''
        return a string representation of the grid for debugging
        '''
        return str(self.cells)

    def get_grid_height(self):
        '''
        get the height of the board
        '''
        return self.grid_height

    def get_grid_width(self):
        '''
        get the width of the board
        '''
        return self.grid_width

    def move(self, direction):
        '''
        move all tiles in the given direction;
        add a new tile if any tiles moved
        '''
        # sliding up, rotate matrix 90' clockwise, merge tiles and rotate it back
        if direction == 1:
            self.cells = zip(*self.cells)[::-1]
            # convert result from tuples back to lists
            self.cells = [list(row) for row in self.cells]
            for row in self.cells:
                merge(row)
            self.cells = zip(*self.cells[::-1])
            self.cells = [list(row) for row in self.cells]

        # sliding down, rotate matrix 90' counter-clockwise, merge tiles and rotate it back
        elif direction == 2:
            self.cells = zip(*self.cells[::-1])
            # convert result from tuples back to lists
            self.cells = [list(row) for row in self.cells]
            for row in self.cells:
                merge(row)
            self.cells = zip(*self.cells)[::-1]
            self.cells = [list(row) for row in self.cells]

        # sliding right, reverse rows (rotate matrix 180'), merge tiles and reverse it back
        elif direction == 4:
            for row in range(len(self.cells)):
                self.cells[row] = self.cells[row][::-1]
            for row in self.cells:
                merge(row)
            for row in range(len(self.cells)):
                self.cells[row] = self.cells[row][::-1]

        # sliding left, just merge tiles as 'to the left' is native merge() feature
        else:
            for row in self.cells:
                merge(row)

        # place new tile after each move
        self.new_tile()

    def new_tile(self):
        '''
        create a new tile in a randomly selected empty square;
        the tile should be 2 90% of the time and 4 10% of the time
        '''
        random_row = random.randint(0, self.grid_width - 1)
        random_col = random.randint(0, self.grid_height - 1)
        random_value = random.choice([2] * 90 + [4] * 10)

        # need to check if there is at least one empty position to place it
        if 0 in [num for elem in self.cells for num in elem]:
            # new tile can be placed in empty space only
            if self.get_tile(random_col, random_row) == 0:
                self.set_tile(random_col, random_row, random_value)
            else:
                self.new_tile()
        else:
            pass

    def set_tile(self, row, col, value):
        '''
        set the tile at position row, col to have the given value
        '''
        self.cells[row][col] = value

    def get_tile(self, row, col):
        '''
        return the value of the tile at position row, col
        '''
        return self.cells[row][col]

# few simple tests
##p = TwentyFortyEight(4, 4)
##print 'width:', p.get_grid_width()
##print 'height:', p.get_grid_height()
##print 'tile at 3, 3 is:', p.get_tile(3, 3)
##p.set_tile(3, 3, 32)
##p.set_tile(3, 0, 2)
##p.set_tile(2, 3, 32)
##p.set_tile(1, 3, 16)
##p.set_tile(1, 0, 16)
##p.set_tile(0, 3, 4)
##p.set_tile(0, 0, 4)
##print 'now tile at 3, 3 is:', p.get_tile(3, 3)
##p.new_tile()
##print p
##p.move(4)
##print 'after one move:'
##print p

# failed tests from the grader
##q = TwentyFortyEight(4, 5)
##q.set_tile(0, 0, 8)
##q.set_tile(0, 1, 16)
##q.set_tile(0, 2, 8)
##q.set_tile(0, 3, 16)
##q.set_tile(0, 4, 8)
##q.set_tile(1, 0, 16)
##q.set_tile(1, 1, 8)
##q.set_tile(1, 2, 16)
##q.set_tile(1, 3, 8)
##q.set_tile(1, 4, 16)
##q.set_tile(2, 0, 8)
##q.set_tile(2, 1, 16)
##q.set_tile(2, 2, 8)
##q.set_tile(2, 3, 16)
##q.set_tile(2, 4, 8)
##q.set_tile(3, 0, 16)
##q.set_tile(3, 1, 8)
##q.set_tile(3, 2, 16)
##q.set_tile(3, 3, 8)
##q.set_tile(3, 4, 16)
##q.move(1)
##print q

##r = TwentyFortyEight(5, 6)
##r.set_tile(0, 0, 0)
##r.set_tile(0, 1, 2)
##r.set_tile(0, 2, 4)
##r.set_tile(0, 3, 8)
##r.set_tile(0, 4, 8)
##r.set_tile(0, 5, 32)
##r.set_tile(1, 0, 16)
##r.set_tile(1, 1, 2)
##r.set_tile(1, 2, 4)
##r.set_tile(1, 3, 16)
##r.set_tile(1, 4, 64)
##r.set_tile(1, 5, 32)
##r.set_tile(2, 0, 0)
##r.set_tile(2, 1, 2)
##r.set_tile(2, 2, 4)
##r.set_tile(2, 3, 8)
##r.set_tile(2, 4, 0)
##r.set_tile(2, 5, 4)
##r.set_tile(3, 0, 16)
##r.set_tile(3, 1, 16)
##r.set_tile(3, 2, 16)
##r.set_tile(3, 3, 16)
##r.set_tile(3, 4, 16)
##r.set_tile(3, 5, 16)
##r.set_tile(4, 0, 16)
##r.set_tile(4, 1, 8)
##r.set_tile(4, 2, 4)
##r.set_tile(4, 3, 4)
##r.set_tile(4, 4, 16)
##r.set_tile(4, 5, 2)
##print r
##r.move(2)
##print r


# helping function to play with cells
def matrix(grid_width, grid_height):
    '''
    helper function to generate array with list comprehension
    '''
    # 'dummy' string is to satisfy pylint rule about unused variables
    cells = [[0 for dummy_col in range(grid_width)] for dummy_row in range(grid_height)]
    return cells

# simple test
##print matrix(4, 4)


# helping function to verify matrix transpose idea
def transpose(listy):
    '''
    helper function to rotate matrix 90' clockwise
    '''
    print 'original matrix:'
    for row in listy:
        print row

    listy = zip(*listy[::-1])
    # convert result from tuples back to lists
    listy = [list(row) for row in listy]

    print 'rotated matrix 90\' clockwise:'
    for row in listy:
        print row

# simple test
##t = transpose(([3, 6, 9], [2, 5, 8], [1, 4, 7]))
##print t


# helping function to test zeros elimination (results in sliding all the tiles)
def eliminate(line):
    '''
    helper function that merges a single row or column in 2048
    '''
    while 0 in line:
        line.remove(0)

    return line

# few simple tests
##print 'elimination zeros follows: '
##print eliminate([0, 0, 0, 1])
##print eliminate([1, 0, 0, 0])
