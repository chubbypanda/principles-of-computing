# Mini-project 5 for Principles of Computing class, by k., 07/18/2014
# Word Wrangler described at: https://class.coursera.org/principlescomputing-001/wiki/view?page=wrangler
# http://www.codeskulptor.org/#poc_wrangler_template.py


# Word Wrangler class from http://www.codeskulptor.org/#poc_wrangler_provided.py

"""
provided code for Word Wrangler game
"""

#import poc_wrangler_gui

class WordWrangler:
    """
    Game class for Word Wrangler
    """
    
    def __init__(self, word_list, remdup, intersect, mergesort, substrs):
        self._word_list = word_list
        self._subset_strings = []
        self._guessed_strings = []

        self._remove_duplicates = remdup
        self._intersect = intersect
        self._merge_sort = mergesort
        self._substrs = substrs

    def start_game(self, entered_word):
        """
        Start a new game of Word Wrangler
        """
        if entered_word not in self._word_list:
            print "Not a word"
            return
        
        strings = self._substrs(entered_word)
        sorted_strings = self._merge_sort(strings)
        all_strings = self._remove_duplicates(sorted_strings)
        self._subset_strings = self._intersect(self._word_list, all_strings)
        self._guessed_strings = []        
        for word in self._subset_strings:
            self._guessed_strings.append("*" * len(word))
        self.enter_guess(entered_word)           
        
    def enter_guess(self, guess):
        """
        Take an entered guess and update the game
        """        
        if ((guess in self._subset_strings) and 
            (guess not in self._guessed_strings)):
            guess_idx = self._subset_strings.index(guess)
            self._guessed_strings[guess_idx] = self._subset_strings[guess_idx]

    def peek(self, peek_index):
        """
        Exposed a word given in index into the list self._subset_strings
        """
        self.enter_guess(self._subset_strings[peek_index])
        
    def get_strings(self):
        """
        Return the list of strings for the GUI
        """
        return self._guessed_strings
    

def run_game(wrangler):
    """
    Start the game.
    """
    poc_wrangler_gui.run_gui(wrangler)
    
    
'''
student code for Word Wrangler game
'''

import urllib2
#import codeskulptor
#import poc_wrangler_provided as provided

WORDFILE = 'assets_scrabble_words3.txt'


# functions to manipulate ordered word lists

def remove_duplicates(list1):
    '''
    eliminate (function can be iterative) duplicates in a sorted list;
    returns a new sorted list with the same elements in list1, without duplicates
    '''
    screened = []
    for item in list1:
        # screening for duplicating items
        if item not in screened:
            screened.append(item)

    return screened

def intersect(list1, list2):
    '''
    compute (this function can be iterative) the intersection of two sorted lists;
    returns a new sorted list containing only elements that are in  both list1 and list2
    '''
    screened = []
    for item in list1:
        # checking for items in common
        if item in list2:
            screened.append(item)
            
    return screened


# functions to perform merge sort

def merge(list1, list2):
    '''
    merge (function can be iterative) two sorted lists;
    returns a new sorted list containing all of the elements that are in either list1 and list2
    '''
    merged = []
    # making copies to avoid list mutation
    copy1, copy2 = list1[:], list2[:]
    while min(copy1, copy2):
        # adding smaller item (and removing it from its list) one by one
        if copy1[0] < copy2[0]:
            merged.append(copy1[0])
            copy1.pop(0)
        else:
            merged.append(copy2[0])
            copy2.pop(0)

    # must include to whatever has been left in longer list (shorter list is empty by now)
    if copy1:
        merged += copy1
    else:
        merged += copy2
   
    return merged
                
def merge_sort(list1):
    '''
    sort (function shall be recursive!) the elements of list1, makes use of merge() function;
    returns a new sorted list with the same elements as list1
    '''
    # base case; for empty/one item lists
    if len(list1) <= 1:
        return list1
    # finding midsection of the list
    half = len(list1) / 2
    
    return merge(merge_sort(list1[:half]), merge_sort(list1[half:]))
    

# function to generate all strings for the word wrangler game

def gen_all_strings(word):
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
    for string in gen_all_strings(word[1:]):
        for index in range(len(string) + 1):
            # inserting the initial character in all possible positions within the string
            possibilities.append(string[:index] + word[0] + string[index:])
            
    return gen_all_strings(word[1:]) + possibilities


# function to load words from a file

def load_words(filename):
    '''
    load word list from the file named filename;
    returns a list of strings
    '''
    try:
        opened_file = open(filename)
    except IOError as e:
        print 'Your scrabble words file is missing.'
     
    return [word[:-1] for word in opened_file]
    
def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# uncomment when you are ready to try the game
# run()
