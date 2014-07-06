# Homework 3 for Principles of Computing class, by k., 07/06/2014

import math
import itertools

# helper functions

def gen_all_sequences(outcomes, length):
    '''
    function that enumerates the set of all sequences of outcomes of given length;
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

#state = gen_all_sequences((1, 2, 3, 4), 2)
#print state, len(state)


# Question 3

def sequence_trials():
    '''
    fair four-sided die (with faces numbered 1-4) is rolled twice
    returns expected value of the product of the two die rolls
    '''
    state = gen_all_sequences((1, 2, 3, 4), 2)
    product = 0
    
    for item in state:
        product += item[0] * item[1]
    return product * 1 / 16.0

print 'Question 3 answer:', sequence_trials()


# Question 4

def sequence_all():
    '''
    what is the probability that this five-digit string consists of five
    consecutive digits in either ascending or descending order (e.g; "34567" or "43210")
    '''
    possibilities = gen_all_sequences((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 5)
    count = 0
    
    for item in possibilities:
        for element in item:
            if all(earlier + 1 == later for earlier, later in zip(item, item[1:])):
                count += 1
    # counter kept track of each element in item (thus 30 / 5), also must count
    # both ascending and descending sequences (thus 6 * 2)
    count /= len(item)
    return count * 2.0 / len(possibilities)

print 'Question 4 answer:', sequence_all()
    

# Question 5

def sequence_perm():
    '''
    what is the probability that this five-digit string consists of five
    consecutive digits in either ascending or descending order (e.g; "34567" or "43210")
    '''
    # same ascending and descending sequences (12 in total) from Question 4
    return 12.0 / (math.factorial(10) / math.factorial(10 - 5))

print 'Question 5 answer:', '{:03.7f}'.format(sequence_perm())


# Question 6

'''
function to generate permutations of outcomes, repetition of outcomes not allowed
provided at: http://www.codeskulptor.org/#poc_permutations_template.py
'''

def gen_permutations(outcomes, length):
    '''
    iterative function that generates set of permutations of outcomes of length num_trials,
    repeated outcomes allowed
    '''  
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                if item not in new_seq:
                    new_seq.append(item)              
                    temp.add(tuple(new_seq))
        ans = temp
    return ans


def run_example():

    # example for digits
    outcome = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #outcome = [0, 1]
    #outcome = ["Red", "Green", "Blue"]
    #outcome = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    length = 2
    permutations = gen_permutations(outcome, length)
    print "Computed", len(permutations), "permutations of length", str(length)
    print "Permutations were", permutations

#run_example()

# test cases output below
#
# computed 90 permutations of length 2
# permutations were set([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)])#
#
# computed 6 permutations of length 2
# permutations were set([('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Red'), ('Green', 'Blue'), ('Blue', 'Red'), ('Blue', 'Green')])
#
# computed 210 permutations of length 3 (result not listed for its extended length)
#Permutations were set([('Sunday', 'Monday', 'Tuesday'), ('Sunday', 'Monday', 'Wednesday'), ('Sunday', 'Monday', 'Thursday'), ('Sunday', 'Monday', 'Friday'), ('Sunday', 'Monday', 'Saturday'), ('Sunday', 'Tuesday', 'Monday'), ('Sunday', 'Tuesday', 'Wednesday'), ('Sunday', 'Tuesday', 'Thursday'), ('Sunday', 'Tuesday', 'Friday'), ('Sunday', 'Tuesday', 'Saturday'), ('Sunday', 'Wednesday', 'Monday'), ('Sunday', 'Wednesday', 'Tuesday'), ('Sunday', 'Wednesday', 'Thursday'), ('Sunday', 'Wednesday', 'Friday'), ('Sunday', 'Wednesday', 'Saturday'), ('Sunday', 'Thursday', 'Monday'), ('Sunday', 'Thursday', 'Tuesday'), ('Sunday', 'Thursday', 'Wednesday'), ('Sunday', 'Thursday', 'Friday'), ('Sunday', 'Thursday', 'Saturday'), ('Sunday', 'Friday', 'Monday'), ('Sunday', 'Friday', 'Tuesday'), ('Sunday', 'Friday', 'Wednesday'), ('Sunday', 'Friday', 'Thursday'), ('Sunday', 'Friday', 'Saturday'), ('Sunday', 'Saturday', 'Monday'), ('Sunday', 'Saturday', 'Tuesday'), ('Sunday', 'Saturday', 'Wednesday'), ('Sunday', 'Saturday', 'Thursday'), ('Sunday', 'Saturday', 'Friday'), ('Monday', 'Sunday', 'Tuesday'), ('Monday', 'Sunday', 'Wednesday'), ('Monday', 'Sunday', 'Thursday'), ('Monday', 'Sunday', 'Friday'), ('Monday', 'Sunday', 'Saturday'), ('Monday', 'Tuesday', 'Sunday'), ('Monday', 'Tuesday', 'Wednesday'), ('Monday', 'Tuesday', 'Thursday'), ('Monday', 'Tuesday', 'Friday'), ('Monday', 'Tuesday', 'Saturday'), ('Monday', 'Wednesday', 'Sunday'), ('Monday', 'Wednesday', 'Tuesday'), ('Monday', 'Wednesday', 'Thursday'), ('Monday', 'Wednesday', 'Friday'), ('Monday', 'Wednesday', 'Saturday'), ('Monday', 'Thursday', 'Sunday'), ('Monday', 'Thursday', 'Tuesday'), ('Monday', 'Thursday', 'Wednesday'), ('Monday', 'Thursday', 'Friday'), ('Monday', 'Thursday', 'Saturday'), ('Monday', 'Friday', 'Sunday'), ('Monday', 'Friday', 'Tuesday'), ('Monday', 'Friday', 'Wednesday'), ('Monday', 'Friday', 'Thursday'), ('Monday', 'Friday', 'Saturday'), ('Monday', 'Saturday', 'Sunday'), ('Monday', 'Saturday', 'Tuesday'), ('Monday', 'Saturday', 'Wednesday'), ('Monday', 'Saturday', 'Thursday'), ('Monday', 'Saturday', 'Friday'), ('Tuesday', 'Sunday', 'Monday'), ('Tuesday', 'Sunday', 'Wednesday'), ('Tuesday', 'Sunday', 'Thursday'), ('Tuesday', 'Sunday', 'Friday'), ('Tuesday', 'Sunday', 'Saturday'), ('Tuesday', 'Monday', 'Sunday'), ('Tuesday', 'Monday', 'Wednesday'), ('Tuesday', 'Monday', 'Thursday'), ('Tuesday', 'Monday', 'Friday'), ('Tuesday', 'Monday', 'Saturday'), ('Tuesday', 'Wednesday', 'Sunday'), ('Tuesday', 'Wednesday', 'Monday'), ('Tuesday', 'Wednesday', 'Thursday'), ('Tuesday', 'Wednesday', 'Friday'), ('Tuesday', 'Wednesday', 'Saturday'), ('Tuesday', 'Thursday', 'Sunday'), ('Tuesday', 'Thursday', 'Monday'), ('Tuesday', 'Thursday', 'Wednesday'), ('Tuesday', 'Thursday', 'Friday'), ('Tuesday', 'Thursday', 'Saturday'), ('Tuesday', 'Friday', 'Sunday'), ('Tuesday', 'Friday', 'Monday'), ('Tuesday', 'Friday', 'Wednesday'), ('Tuesday', 'Friday', 'Thursday'), ('Tuesday', 'Friday', 'Saturday'), ('Tuesday', 'Saturday', 'Sunday'), ('Tuesday', 'Saturday', 'Monday'), ('Tuesday', 'Saturday', 'Wednesday'), ('Tuesday', 'Saturday', 'Thursday'), ('Tuesday', 'Saturday', 'Friday'), ('Wednesday', 'Sunday', 'Monday'), ('Wednesday', 'Sunday', 'Tuesday'), ('Wednesday', 'Sunday', 'Thursday'), ('Wednesday', 'Sunday', 'Friday'), ('Wednesday', 'Sunday', 'Saturday'), ('Wednesday', 'Monday', 'Sunday'), ('Wednesday', 'Monday', 'Tuesday'), ('Wednesday', 'Monday', 'Thursday'), ('Wednesday', 'Monday', 'Friday'), ('Wednesday', 'Monday', 'Saturday'), ('Wednesday', 'Tuesday', 'Sunday'), ('Wednesday', 'Tuesday', 'Monday'), ('Wednesday', 'Tuesday', 'Thursday'), ('Wednesday', 'Tuesday', 'Friday'), ('Wednesday', 'Tuesday', 'Saturday'), ('Wednesday', 'Thursday', 'Sunday'), ('Wednesday', 'Thursday', 'Monday'), ('Wednesday', 'Thursday', 'Tuesday'), ('Wednesday', 'Thursday', 'Friday'), ('Wednesday', 'Thursday', 'Saturday'), ('Wednesday', 'Friday', 'Sunday'), ('Wednesday', 'Friday', 'Monday'), ('Wednesday', 'Friday', 'Tuesday'), ('Wednesday', 'Friday', 'Thursday'), ('Wednesday', 'Friday', 'Saturday'), ('Wednesday', 'Saturday', 'Sunday'), ('Wednesday', 'Saturday', 'Monday'), ('Wednesday', 'Saturday', 'Tuesday'), ('Wednesday', 'Saturday', 'Thursday'), ('Wednesday', 'Saturday', 'Friday'), ('Thursday', 'Sunday', 'Monday'), ('Thursday', 'Sunday', 'Tuesday'), ('Thursday', 'Sunday', 'Wednesday'), ('Thursday', 'Sunday', 'Friday'), ('Thursday', 'Sunday', 'Saturday'), ('Thursday', 'Monday', 'Sunday'), ('Thursday', 'Monday', 'Tuesday'), ('Thursday', 'Monday', 'Wednesday'), ('Thursday', 'Monday', 'Friday'), ('Thursday', 'Monday', 'Saturday'), ('Thursday', 'Tuesday', 'Sunday'), ('Thursday', 'Tuesday', 'Monday'), ('Thursday', 'Tuesday', 'Wednesday'), ('Thursday', 'Tuesday', 'Friday'), ('Thursday', 'Tuesday', 'Saturday'), ('Thursday', 'Wednesday', 'Sunday'), ('Thursday', 'Wednesday', 'Monday'), ('Thursday', 'Wednesday', 'Tuesday'), ('Thursday', 'Wednesday', 'Friday'), ('Thursday', 'Wednesday', 'Saturday'), ('Thursday', 'Friday', 'Sunday'), ('Thursday', 'Friday', 'Monday'), ('Thursday', 'Friday', 'Tuesday'), ('Thursday', 'Friday', 'Wednesday'), ('Thursday', 'Friday', 'Saturday'), ('Thursday', 'Saturday', 'Sunday'), ('Thursday', 'Saturday', 'Monday'), ('Thursday', 'Saturday', 'Tuesday'), ('Thursday', 'Saturday', 'Wednesday'), ('Thursday', 'Saturday', 'Friday'), ('Friday', 'Sunday', 'Monday'), ('Friday', 'Sunday', 'Tuesday'), ('Friday', 'Sunday', 'Wednesday'), ('Friday', 'Sunday', 'Thursday'), ('Friday', 'Sunday', 'Saturday'), ('Friday', 'Monday', 'Sunday'), ('Friday', 'Monday', 'Tuesday'), ('Friday', 'Monday', 'Wednesday'), ('Friday', 'Monday', 'Thursday'), ('Friday', 'Monday', 'Saturday'), ('Friday', 'Tuesday', 'Sunday'), ('Friday', 'Tuesday', 'Monday'), ('Friday', 'Tuesday', 'Wednesday'), ('Friday', 'Tuesday', 'Thursday'), ('Friday', 'Tuesday', 'Saturday'), ('Friday', 'Wednesday', 'Sunday'), ('Friday', 'Wednesday', 'Monday'), ('Friday', 'Wednesday', 'Tuesday'), ('Friday', 'Wednesday', 'Thursday'), ('Friday', 'Wednesday', 'Saturday'), ('Friday', 'Thursday', 'Sunday'), ('Friday', 'Thursday', 'Monday'), ('Friday', 'Thursday', 'Tuesday'), ('Friday', 'Thursday', 'Wednesday'), ('Friday', 'Thursday', 'Saturday'), ('Friday', 'Saturday', 'Sunday'), ('Friday', 'Saturday', 'Monday'), ('Friday', 'Saturday', 'Tuesday'), ('Friday', 'Saturday', 'Wednesday'), ('Friday', 'Saturday', 'Thursday'), ('Saturday', 'Sunday', 'Monday'), ('Saturday', 'Sunday', 'Tuesday'), ('Saturday', 'Sunday', 'Wednesday'), ('Saturday', 'Sunday', 'Thursday'), ('Saturday', 'Sunday', 'Friday'), ('Saturday', 'Monday', 'Sunday'), ('Saturday', 'Monday', 'Tuesday'), ('Saturday', 'Monday', 'Wednesday'), ('Saturday', 'Monday', 'Thursday'), ('Saturday', 'Monday', 'Friday'), ('Saturday', 'Tuesday', 'Sunday'), ('Saturday', 'Tuesday', 'Monday'), ('Saturday', 'Tuesday', 'Wednesday'), ('Saturday', 'Tuesday', 'Thursday'), ('Saturday', 'Tuesday', 'Friday'), ('Saturday', 'Wednesday', 'Sunday'), ('Saturday', 'Wednesday', 'Monday'), ('Saturday', 'Wednesday', 'Tuesday'), ('Saturday', 'Wednesday', 'Thursday'), ('Saturday', 'Wednesday', 'Friday'), ('Saturday', 'Thursday', 'Sunday'), ('Saturday', 'Thursday', 'Monday'), ('Saturday', 'Thursday', 'Tuesday'), ('Saturday', 'Thursday', 'Wednesday'), ('Saturday', 'Thursday', 'Friday'), ('Saturday', 'Friday', 'Sunday'), ('Saturday', 'Friday', 'Monday'), ('Saturday', 'Friday', 'Tuesday'), ('Saturday', 'Friday', 'Wednesday'), ('Saturday', 'Friday', 'Thursday')])

outcome = set(['a', 'b', 'c', 'd', 'e', 'f'])

permutations = gen_permutations(outcome, 4)
permutation_list = list(permutations)
permutation_list.sort()
print 'Question 6 answer:', permutation_list[100]


# Question 7

def powerset(sets):
    '''
    just generate a power set

    sets (a tuple): original set
    returns a set of tuples
    '''
    all_set = [()]
    for item in sets:
        for subset in all_set:
            all_set = all_set + [tuple(subset) + (item, )]
           
    return all_set

print 'Question 7 answer:', powerset((1, 2))

# Question 8

print '\nPrep for Question 8 follows...'
print 'when n is 0:', len(powerset(())), powerset(())
print 'when n is 1:', len(powerset((1, ))), powerset((1, ))
print 'when n is 2:', len(powerset((1, 2))), powerset((1, 2))
print 'when n is 3:', len(powerset((1, 2, 3))), powerset((1, 2, 3))
print 'when n is 4:', len(powerset((1, 2, 3, 4))), powerset((1, 2, 3, 4))
print 'when n is 5:', len(powerset((1, 2, 3, 4, 5))), '(powerset output omitted, too long)'
print 'when n is 6:', len(powerset((1, 2, 3, 4, 5, 6))), '(powerset output omitted, too long)'
print 'when n is 7:', len(powerset((1, 2, 3, 4, 5, 6, 7))), '(powerset output omitted, too long)'
print 'when n is 8:', len(powerset((1, 2, 3, 4, 5, 6, 7, 8))), '(powerset output omitted, too long)', '\n'


# Question 9

def comb():
    '''
    what is the probability of being dealt a five card hand where all five cards are of the same suit?
    '''
    all_five = 4.0 * math.factorial(13) / (math.factorial(13 - 5) * math.factorial(5))
    combination_total = math.factorial(52) / (math.factorial(52 - 5) * math.factorial(5))

    return all_five / combination_total

print "Question 9 answer:", comb()
