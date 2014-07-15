# Homework 4 for Principles of Computing class, by k., 07/15/2014

# Question 6

"""
Grid class from http://www.codeskulptor.org/#poc_grid.py
"""

EMPTY = 0
FULL = 1

class Grid:
    """
    Implementation of 2D grid of cells
    Includes boundary handling
    """
    
    def __init__(self, grid_height, grid_width):
        """
        Initializes grid to be empty, take height and width of grid as parameters
        Indexed by rows (left to right), then by columns (top to bottom)
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._cells = [[EMPTY for dummy_col in range(self._grid_width)] 
                       for dummy_row in range(self._grid_height)]
                
    def __str__(self):
        """
        Return multi-line string represenation for grid
        """
        ans = ""
        for row in range(self._grid_height):
            ans += str(self._cells[row])
            ans += "\n"
        return ans
    
    def get_grid_height(self):
        """
        Return the height of the grid for use in the GUI
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Return the width of the grid for use in the GUI
        """
        return self._grid_width


    def clear(self):
        """
        Clears grid to be empty
        """
        self._cells = [[EMPTY for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]
                
    def set_empty(self, row, col):
        """
        Set cell with index (row, col) to be empty
        """
        self._cells[row][col] = EMPTY
    
    def set_full(self, row, col):
        """
        Set cell with index (row, col) to be full
        """
        self._cells[row][col] = FULL
    
    def is_empty(self, row, col):
        """
        Checks whether cell with index (row, col) is empty
        """
        return self._cells[row][col] == EMPTY
 
    def four_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col)
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self._grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self._grid_width - 1:
            ans.append((row, col + 1))
        return ans

    def four_neighbors_wrapped(self, row, col):
        '''
        returns horiz/vert neighbors of cell (row, col) for wrapping scenario
        '''
        up = (row - 1) % self._grid_height
        down = (row + 1) % self._grid_height
        left = (col - 1) % self._grid_width
        right = (col + 1) % self._grid_width
        return [(up, col), (down, col), (row, left), (row, right)]

    def eight_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col) as well as
        diagonal neighbors
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self._grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self._grid_width - 1:
            ans.append((row, col + 1))
        if (row > 0) and (col > 0):
            ans.append((row - 1, col - 1))
        if (row > 0) and (col < self._grid_width - 1):
            ans.append((row - 1, col + 1))
        if (row < self._grid_height - 1) and (col > 0):
            ans.append((row + 1, col - 1))
        if (row < self._grid_height - 1) and (col < self._grid_width - 1):
            ans.append((row + 1, col + 1))
        return ans
    
    def get_index(self, point, cell_size):
        """
        Takes point in screen coordinates and returns index of
        containing cell
        """
        return (point[1] / cell_size, point[0] / cell_size) 


print 'Question 6 check...'
state = Grid(6, 9)
print 'When boundaries considered as impassable:', state.four_neighbors(0, 6)
print 'When boundaries wraps around:', state.four_neighbors_wrapped(0, 6)


# Question 9

'''
implemented stack class, template at http://www.codeskulptor.org/#poc_stack_template.py
'''

class Stack:
    '''
    a simple implementation of a FILO (stack)
    '''

    def __init__(self):
        ''' 
        initialize the stack
        '''
        self._stack = []

    def __len__(self):
        '''
        return number of items in the stack
        '''
        return len(self._stack)

    def __str__(self):
        '''
        returns a string representation of the stack
        '''
        return str(self._stack)

    def push(self, item):
        '''
        push item onto the stack
        '''
        self._stack.insert(0, item)

    def pop(self):
        '''
        pop an item off of the stack
        '''
        return self._stack.pop(0)

    def clear(self):
        """
        Remove all items from the stack.
        """
        self._stack = []


# test code for the stack

my_stack = Stack()
my_stack.push(72)
my_stack.push(59)
my_stack.push(33)
my_stack.pop()
my_stack.push(77)
my_stack.push(13)
my_stack.push(22)
my_stack.push(45)
my_stack.pop()
my_stack.pop()
my_stack.push(22)
my_stack.push(72)
my_stack.pop()
my_stack.push(90)
my_stack.push(67)
while len(my_stack) > 4:
    my_stack.pop()
my_stack.push(32)
my_stack.push(14)
my_stack.pop()
my_stack.push(65)
my_stack.push(87)
my_stack.pop()
my_stack.pop()
my_stack.push(34)
my_stack.push(38)
my_stack.push(29)
my_stack.push(87)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print '\nQuestion 9 answer:', my_stack.pop()


# Question 10

'''
modified queue class from hhttp://www.codeskulptor.org/#poc_queue.py
'''

class Queue:
    '''
    a simple implementation of a FIFO (queue)
    '''

    def __init__(self):
        '''
        initialize the queue
        '''
        self._queue = []

    def __len__(self):
        '''
        return the number of items in the queue
        '''
        return len(self._queue)
    
    def __iter__(self):
        '''
        create an iterator for the queue
        '''
        for item in self._queue:
            yield item

    def __str__(self):
        '''
        return a string representation of the queue
        '''
        return str(self._queue)

    def enqueue(self, item):
        '''
        add item to the queue (altered to act as a push)
        '''        
        self._queue.insert(0, item)

    def dequeue(self):
        '''
        remove and return the least recently inserted item (altered to act as a pop)
        '''
        return self._queue.pop(0)

    def clear(self):
        '''
        remove all items from the queue
        '''
        self._queue = []
        

# this question requires to use provided GUI in obscure interpreter from the class,
# uploaded to: http://www.codeskulptor.org/#user36_su4XOw8EJE_0.py
