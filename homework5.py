# Homework 5 for Principles of Computing class, by k., 07/19/2014

# Question 1

class Incrementer(object):
    '''
    counting increments separately from the function
    '''
    def __init__(self, count):
        self.count = count

    def increment(self):
        self.count += 1

"""
Recursion according to the "Cat in the Hat"
"""

def get_next_cat(current_cat):
    """
    Helper function to get next cat
    """
    if current_cat == "Cat in the Hat":
        return "Little Cat A"
    elif current_cat != "Little Cat Z":
        return "Little Cat " + chr(ord(current_cat[-1]) + 1)
    else:
        return "Voom"

def clean_up(helper_cat):
    """
    Recursive function that prints out story
    """
    if helper_cat == "Voom":
        print helper_cat + ": I got this. Mess is all cleaned up!"
    else:
        next_cat = get_next_cat(helper_cat)
        print helper_cat + ": I'll have", next_cat, "clean up!"
        clean_up(next_cat)
        i.increment()
        
# get those cats to work!!!!!
print 'Question 1 prep...'
i = Incrementer(0)
clean_up("Cat in the Hat")
i.increment()
print 'Question 1 answer:', i.count


# Question 2

def add_up(n):
    if n == 0:
        return 0
    else:
        return n + add_up(n - 1)

print '\nPrep for Question 2 follows...'
print 'when n is 0:', add_up(0)
print 'when n is 1:', add_up(1)
print 'when n is 2:', add_up(2)
print 'when n is 3:', add_up(3)
print 'when n is 4:', add_up(4)
print 'when n is 5:', add_up(5)
print 'when n is 6:', add_up(6)
print 'when n is 7:', add_up(7)
print 'when n is 8:', add_up(8)


# Question 3

def multiply_up(n):
    if n == 0:
        return 1
    else:
        return n * multiply_up(n - 1)

print '\nPrep for Question 3 follows...'
print 'when n is 0:', multiply_up(0)
print 'when n is 1:', multiply_up(1)
print 'when n is 2:', multiply_up(2)
print 'when n is 3:', multiply_up(3)
print 'when n is 4:', multiply_up(4)
print 'when n is 5:', multiply_up(5)
print 'when n is 6:', multiply_up(6)
print 'when n is 7:', multiply_up(7)
print 'when n is 8:', multiply_up(8)


# Question 4

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        j.increment()
        return fib(num - 1) + fib(num - 2)

print '\nPrep for Question 4 follows...'
j = Incrementer(0)
fib(2)
print 'when n is 2:', j.count
j = Incrementer(0)
fib(3)
print 'when n is 3:', j.count
j = Incrementer(0)
fib(4)
print 'when n is 4:', j.count
j = Incrementer(0)
fib(5)
print 'when n is 5:', j.count
j = Incrementer(0)
fib(6)
print 'when n is 6:', j.count
j = Incrementer(0)
fib(7)
print 'when n is 7:', j.count
j = Incrementer(0)
fib(8)
print 'when n is 8:', j.count


# Question 5

def memoized_fib(num, memo_dict):
    k.increment()
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        #k.increment()
        sum2 = memoized_fib(num - 2, memo_dict)
        #k.increment()
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2

print '\nPrep for Question 5 follows...'
k = Incrementer(0)
memoized_fib(0, {0 : 0, 1 : 1})
print 'when n is 0:', k.count
k = Incrementer(0)
memoized_fib(1, {0 : 0, 1 : 1})
print 'when n is 1:', k.count
k = Incrementer(0)
memoized_fib(2, {0 : 0, 1 : 1})
print 'when n is 2:', k.count
k = Incrementer(0)
memoized_fib(3, {0 : 0, 1 : 1})
print 'when n is 3:', k.count
k = Incrementer(0)
memoized_fib(4, {0 : 0, 1 : 1})
print 'when n is 4:', k.count
k = Incrementer(0)
memoized_fib(5, {0 : 0, 1 : 1})
print 'when n is 5:', k.count
k = Incrementer(0)
memoized_fib(6, {0 : 0, 1 : 1})
print 'when n is 6:', k.count
k = Incrementer(0)
memoized_fib(7, {0 : 0, 1 : 1})
print 'when n is 7:', k.count


# Question 6

def outcomes(word):
    '''
    generate (function shall be recursive!) all strings that can be composed
    from the letters in word in any order;
    returns a list of all strings that can be formed from the letters in word
    '''
    # base case; no string
    if not word:
        return ['']
    
    possibilities = []
    # generate all appropriate strings for rest of the word
    for string in outcomes(word[1:]):
        l.increment()
        for index in range(len(string) + 1):
            # inserting the initial character in all possible positions within the string
            possibilities.append(string[:index] + word[0] + string[index:])
    l.increment()
    return outcomes(word[1:]) + possibilities

print '\nPrep for Question 6 follows...'
l = Incrementer(0)
outcomes('a')
print 'when n is 1:', l.count
l = Incrementer(0)
outcomes('ab')
print 'when n is 2:', l.count
l = Incrementer(0)
outcomes('abc')
print 'when n is 3:', l.count
l = Incrementer(0)
outcomes('abcd')
print 'when n is 4:', l.count
l = Incrementer(0)
outcomes('abcde')
print 'when n is 5:', l.count
l = Incrementer(0)
outcomes('abcdef')
print 'when n is 6:', l.count
l = Incrementer(0)
outcomes('abcdefg')
print 'when n is 7:', l.count
