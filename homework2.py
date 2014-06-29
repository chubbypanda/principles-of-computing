# Homework 2 for Principles of Computing class, by k., 06/29/2014

import math
import random

# Question 3

def specific_suite():
    '''
    probability that the card will be of a specific suit
    a standard deck of 52 playings cards (4 suits with 13 cards in each suit)
    '''
    return 13 / 52.0

print 'Question 3 answer:', specific_suite()


# Question 4

def possible_outcomes_36():
    '''
    a trial with possible outcomes where each outcome has equal probability,
    how many outcomes correspond to an event that has probability
    '''
    return 36 * 1/9

print 'Question 4 answer:', possible_outcomes_36()


def gpas():
    '''
    a trial with possible outcomes where each outcome has equal probability,
    how many outcomes correspond to an event that has probability
    '''
    return (4.0 * 30 + 3.0 * 40 + 2.0 * 20 + 1.0 * 10) / 100

print 'Question 7 answer:', gpas()

# Question 9

def trial(n):
    '''
    expected value of trial(n) as a function of n
    '''
    val = random.randrange(n)
    return val

print '\nPrep for Question 9 follows...'
print 'when n is 1: ', trial(1)
print 'when n is 10: ', trial(10)
print 'when n is 100: ', trial(100)
print 'when n is 1000: ', trial(1000)

# for n = 10: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# thus (0, 1, 2, ..., n - 1) * 1/n
# (where 1/n is probability of each possible outcome)

def total_sum_full(n):
    if n == 0:
        return 0
    return n + total_sum_full(n - 1)

def total_sum_mins(n):
    return (n + 1)/2 * n

print 'for value 99 sum is:', total_sum_mins(99), ', and its expected average is:', total_sum_mins(99) / 100
# answer is: (n - 1)/2


# Question 10

''' 
program that computes mystery number
'''

def inside_unit_circle(point):
    '''
    compute distance of point from origin
    '''
    distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
    return distance < 1
                                                 

def estimate_mystery(num_trials):
    '''
    main function
    '''
    num_inside = 0
    
    for dumm_idx in range(num_trials):
        new_point = [2 * random.random() - 1, 2 * random.random() - 1]
        if inside_unit_circle(new_point):
            num_inside += 1
    
    return float(num_inside) / num_trials

print '\nQuestion 10\'s mystery number:', estimate_mystery(10000)
print 'As compared to pi/4 (4, as there are four quadrants in a circle):', math.pi / 4
