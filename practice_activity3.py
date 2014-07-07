# Practice Activity 3 for Principles of Computing class, by k., 07/04/2014
# Analyzing a simple dice game (see https://class.coursera.org/principlescomputing-001/wiki/dice_game )
# skeleton code: http://www.codeskulptor.org/#poc_dice_game_template.py
# official solution: http://www.codeskulptor.org/#poc_dice_game_solution.py

'''
analyzing a simple dice game
'''

def gen_all_sequences(outcomes, length):
    '''
    iterative function that enumerates the set of all sequences of
    outcomes of given length
    '''
    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

# example for digits
#print gen_all_sequences([1, 2, 3, 4, 5, 6], 2)

  
def max_repeats(seq):
    '''
    compute the maximum number of times that an outcome is repeated in a sequence
    '''
    acc = []
    # counting number of occurances for each item in a sequence
    for item in seq:
        acc.append(seq.count(item))
    return max(acc)
    
#print max_repeats((3, 3, 3))
#print max_repeats((6, 6, 2))


def compute_expected_value():
    '''
    computes expected value of simple dice game, pay the initial $10,
    gain for double is $10, gain for triple is $200
    '''
    doubles = 0
    triples = 0
    seq = gen_all_sequences([1, 2, 3, 4, 5, 6], 3)

    # searching for doubles and triples in generated sequence
    for item in seq:
        if max_repeats(item) == 2:
            doubles += 1
        elif max_repeats(item) == 3:
            triples += 1
    # probability is frequency divided by all possible results
    doubles /= float(len(seq))
    triples /= float(len(seq))
    
    return doubles * 10 + triples * 200

#print compute_expected_value()


def run_test():
    '''
    testing code, note that the initial cost of playing the game has been subtracted
    '''
    outcomes = set([1, 2, 3, 4, 5, 6])
    print 'All possible sequences of three dice are'
    print gen_all_sequences(outcomes, 3)
    print
    print 'Test for max repeats'
    print 'Max repeat for (3, 1, 2) is', max_repeats((3, 1, 2))
    print 'Max repeat for (3, 3, 2) is', max_repeats((3, 3, 2))
    print 'Max repeat for (3, 3, 3) is', max_repeats((3, 3, 3))
    print
    print 'Ignoring the initial $10, the expected value was $', compute_expected_value()
    
run_test()
