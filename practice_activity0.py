# Practice Activity 0 for Principles of Computing class, by k., 06/18/2014
# Solitaire Mancala; GUI is provided in codeskulptor (obscure Python interpretter for the class) at:
# http://www.codeskulptor.org/#poc_mancala_gui.py

  
class SolitaireMancala(object):
    '''
    class to run the game logic
    '''
    def __init__(self):
        self.state = [0]
        
    def set_board(self, configuration):
        '''
        board to be a copy of the supplied configuration
        '''
        self.state = configuration[:]
        
    def __str__(self):
        '''
        string corresponding to the current configuration of the board
        '''
        # logic of the game and internal representation are reversed
        return str(self.state[::-1])
        
    def get_num_seeds(self, house_num):
        '''
        return the number of seeds in the house with index house_num
        '''
        return self.state[house_num]        

    def is_legal_move(self, house_num):
        '''
        return True if moving the seeds from house house_num is legal;
        if house_num is zero, is_legal_move should return False
        '''
        # a move is legal if house value equals to its distance from the store
        return self.state[house_num] == house_num and house_num != 0

    def is_game_won(self):
        '''
        return True if all houses contain no seeds
        '''
        # check if all positions (except for the store) are empty
        return sum(self.state[1:]) == 0
    
    def apply_move(self, house_num):
        '''
        apply a legal move for house house_num to the board
        '''
        if self.is_legal_move(house_num):
            # adding +1 to each position lying in front of (and excluding) house_num
            for position in xrange(len(self.state[:house_num])):
                self.state[position] += 1
            # current house (house_num) is then emptied
            self.state[house_num] = 0
        else:
            print 'No can do, this is a illegal move!'
    
    def choose_move(self):
        '''
        return the index for the legal move whose house is closest to the store;
        if no legal move is available, return 0
        '''
        # if no legal move found, need to eventually return 0
        index = 0
        # checking through each position backwards just to arrive at closest one
        for num in range(len(self.state))[::-1]:
            if self.is_legal_move(num):
                index = num
        return index

    def plan_moves(self):
        '''
        return a list of legal moves computed to win the game if possible
        '''
        legal_moves = []
        # game isn't won yet and there is still at least one legal move
        while not self.is_game_won() and self.choose_move() != 0:
            # make a note of and apply every possible move suggested
            legal_moves.append(self.choose_move())
            self.apply_move(self.choose_move())
        return legal_moves


# few simple tests
##p = SolitaireMancala()
##print p
##p.set_board([3, 1, 1, 1, 1, 1, 1])
##print p
##print p.get_num_seeds(3)
##print 'game won?', p.is_game_won()
##p.set_board([3, 0, 0, 0, 0, 0, 0])
##print p
##print 'game won?', p.is_game_won()
##p.set_board([0, 6, 5, 4, 3, 2, 1])
##print p.is_legal_move(6), p.is_legal_move(5), p.is_legal_move(4)
##p.set_board([0, 1, 2, 3, 5, 4, 6])
##print p.is_legal_move(6), p.is_legal_move(5), p.is_legal_move(4), p.is_legal_move(0)
##print p
##print p.choose_move()
##p.apply_move(0)
##print 'before move:', p
##p.apply_move(6)
##print 'after move :', p
##print p.choose_move()
##print 'before move:', p
##p.apply_move(5)
##print 'after move :', p
##p.apply_move(4)
##print p.choose_move()
##p.plan_moves()
##print
##q = SolitaireMancala()
##q.set_board([0, 1, 2, 2, 4, 0, 0])
##print 'before game:   ', q
##print q.choose_move()
##q.plan_moves()
##print q.is_game_won()
##print 'game finished:', q

# checking tests 5a and 5b from the grader
##test5a = SolitaireMancala()
##test5a.set_board([0, 0, 1, 1, 3, 5])
##print test5a.choose_move(), type(test5a.choose_move())
##test5b = SolitaireMancala()
##test5b.set_board([0, 0, 1, 1, 3, 0, 0])
##print test5b.choose_move(), type(test5b.choose_move())
##print test5a.is_legal_move(0)
##print test5b.is_legal_move(0)
##print test5a.choose_move()
##game = SolitaireMancala()
##SolitaireMancala.set_board(game, [0,0,1])
##print SolitaireMancala.plan_moves(game)
##print SolitaireMancala.is_game_won(game)
    
# failed test 6c from the grader
##game = SolitaireMancala()
##SolitaireMancala.set_board(game, [0,0,1])
##SolitaireMancala.plan_moves(game)
##print SolitaireMancala.plan_moves(game)
##print SolitaireMancala.is_game_won(game)
