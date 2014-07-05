# Mini-project 3 for Principles of Computing class, by k., 07/04/2014
# Yahtzee (simplified) described at: https://class.coursera.org/principlescomputing-001/wiki/view?page=yahtzee
# http://www.codeskulptor.org/#poc_yahtzee_template.py


# optional test suite (obscure suite provided for the class; ignore it) from: 
# http://www.codeskulptor.org/#poc_holds_testsuite.py

"""
Test suite for gen_all_holds in "Yahtzee"
"""

##import poc_simpletest
##
##def run_suite(gen_all_holds):
##    """
##    Some informal testing code for gen_all_holds
##    """
##    
##    # create a TestSuite object
##    suite = poc_simpletest.TestSuite()
##    
##    # test gen_all_holds on various inputs
##    hand = tuple([])
##    suite.run_test(gen_all_holds(hand), set([()]), "Test #1:")
##
##    hand = tuple([4, 2])
##    suite.run_test(gen_all_holds(hand), set([(), (4,), (2,), (4, 2)]), "Test #2:")
##    
##    hand = tuple((1, 2, 2))
##    suite.run_test(gen_all_holds(hand), set([(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)]), "Test #3:")
##
##    hand = tuple((2, 1, 2))
##    suite.run_test(gen_all_holds(hand), set([(), (1,), (2,), (1, 2), (2, 1), (2, 2), (2, 1, 2)]), "Test #4:")
##
##    hand = tuple([6, 2, 3])
##    suite.run_test(gen_all_holds(hand),set([(), (6,), (2,), (6, 2), (3,), (6, 3), (2, 3), (6, 2, 3)]), "Test #5:")
##
##    suite.report_results()
##    


'''
planner for Yahtzee
simplified (only allow discard and roll, only score against upper level)
'''

# used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)


def gen_all_sequences(outcomes, length):
    '''
    iterative function that enumerates the set of all sequences of outcomes of given length;
    original code from the lecture, do not modify
    '''
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    '''
    compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card

    hand (die values in a tuple): full yahtzee hand

    returns an integer score
    '''
    # empty hand returns 0, naturally
    if not hand:
        return 0
    
    maximum_score = []
    for item in hand:
        # value is determined by its frequency and denomination
        maximum_score.append(hand.count(item) * item)
    return max(maximum_score)


def expected_value(held_dice, num_die_sides, num_free_dice):
    '''
    compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides

    held_dice (a tuple): dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    returns a floating point expected value
    '''
    # commented out for testing stage (too many tests violates game premise)
##    try:
##        assert len(held_dice) + num_free_dice == 5
##        assert num_die_sides == 6
##    except:
##        print 'Standard Yahtzee game shall use precisely five dice (each with six sides)!'

    scores = []
    die_sides = [die for die in range(1, num_die_sides + 1)]
    possible_sequence = gen_all_sequences(die_sides, num_free_dice)

    # scoring sum of held dice with each generated possibility
    for item in possible_sequence:
        scores.append(score(held_dice + item))
    
    return float(sum(scores)) / len(scores)

    
def gen_all_holds(hand):
    '''
    generate all possible choices of dice from hand to hold

    hand (a tuple): full yahtzee hand

    returns a set of tuples, where each tuple is dice to hold
    '''
    # just generate a power set from 'hand' (without following recipe with itertools)
    from_hand = [()]
    for item in hand:
        for subset in from_hand:
            from_hand = from_hand + [tuple(subset) + (item, )]
           
    return set(from_hand)
            
    
def strategy(hand, num_die_sides):
    '''
    compute the hold that maximizes the expected value when the discarded dice are rolled

    hand (a tuple): full yahtzee hand
    num_die_sides: number of sides on each die

    returns a tuple (where the first element is the expected score,
    the second element is a tuple of the dice to hold)
    '''
    result = (0.0, ())
    current_value = float('-inf')
    
    for item in gen_all_holds(hand):
        # looking for maximum value, keeping track along the way
        value = expected_value(item, num_die_sides, len(hand) - len(item))
        if value > current_value:
            current_value = value
            result = (current_value, item)
    
    return result

#print strategy((1,), 6)
#print strategy((1, 8, 8), 6)

def run_example():
    '''
    compute the dice to hold and expected score for an example hand
    '''
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print 'Best strategy for hand', hand, 'is to hold', hold, 'with expected score', hand_score
    
    
#run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
