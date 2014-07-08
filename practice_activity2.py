# Practice Activity 2 for Principles of Computing class, by k., 07/07/2014
# simplified Nim (Monte Carlo solver) (see https://class.coursera.org/principlescomputing-001/wiki/view?page=nim_mc )
# template: http://www.codeskulptor.org/#poc_nim_mc_template.py
# official solution: http://www.codeskulptor.org/#poc_nim_mc_student.py

'''
a simple Monte Carlo solver for Nim (http://en.wikipedia.org/wiki/Nim#The_21_game )
'''

import random
#import codeskulptor
#codeskulptor.set_timeout(20)


MAX_REMOVE = 3
TRIALS = 10000

def evaluate_position(num_items):
    '''
    Monte Carlo evalation method for Nim
    '''
    max_computer_wins = float('-inf')
    for move in range(1, (MAX_REMOVE) + 1):
        computer_wins = 0
        for trial in range(TRIALS):
            initial_move = move
            current_items = num_items - initial_move
            
            while True:
                # play & evaluate player's move
                generated_move = random.choice(range(1, (MAX_REMOVE) + 1))
                current_items -= generated_move
                if current_items <= 0:
                    break
                # play & evaluate computer's move
                generated_move = random.choice(range(1, (MAX_REMOVE) + 1))
                current_items -= generated_move
                if current_items <= 0:
                    computer_wins += 1
                    break

        # keeping track of best value amongst (1, 2, 3) initial moves
        if max_computer_wins < computer_wins:
            result = move
            max_computer_wins = computer_wins
            
        #print 'For', move, 'Computer won:', computer_wins, 'Player won:', TRIALS - computer_wins
    return result
        
#print evaluate_position(10)

# optimal strategy: when your turn to move, remove exactly enough items so that the number of items
# remaining in the heap has remainder zero when divided by four     


def play_game(start_items):
    '''
    play a game of Nim against Monte Carlo bot
    '''
    
    current_items = start_items
    print 'Starting game with value', current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print 'Computer choose', comp_move, ', current value is', current_items
        if current_items <= 0:
            print 'Computer wins'
            break
        player_move = int(input('Enter your current move: '))
        current_items -= player_move
        print 'Player choose', player_move, ', current value is', current_items
        if current_items <= 0:
            print 'Player wins'
            break

#play_game(21)
# quick test
#play_game(10)
