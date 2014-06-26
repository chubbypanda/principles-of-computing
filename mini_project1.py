# Mini-project 1 for Principles of Computing class, by k., 06/22/2014
# clone of Cookie Clicker; simpleplot needs codeskulptor (obscure Python interpretter for the class) at:
# https://class.coursera.org/principlescomputing-001/wiki/view?page=clicker
# http://www.codeskulptor.org/#poc_clicker_template.py


# BuildInfo Class described and stored at: 
# https://class.coursera.org/principlescomputing-001/wiki/BuildInfo
# http://www.codeskulptor.org/#poc_clicker_provided.py

'''
Cookie Clicker Simulator Build Information
'''

BUILD_GROWTH = 1.15

class BuildInfo:
    """
    Class to track build information.
    """
    
    def __init__(self, build_info = None, growth_factor = BUILD_GROWTH):
        self._build_growth = growth_factor
        if build_info == None:
            self._info = {"Cursor": [15.0, 0.1],
                          "Grandma": [100.0, 0.5],
                          "Farm": [500.0, 4.0],
                          "Factory": [3000.0, 10.0],
                          "Mine": [10000.0, 40.0],
                          "Shipment": [40000.0, 100.0],
                          "Alchemy Lab": [200000.0, 400.0],
                          "Portal": [1666666.0, 6666.0],
                          "Time Machine": [123456789.0, 98765.0],
                          "Antimatter Condenser": [3999999999.0, 999999.0]}
        else:
            self._info = {}
            for key, value in build_info.items():
                self._info[key] = list(value)
            
    def build_items(self):
        """
        Get a list of buildable items
        """
        return self._info.keys()
            
    def get_cost(self, item):
        """
        Get the current cost of an item
        Will throw a KeyError exception if item is not in the build info.
        """
        return self._info[item][0]
    
    def get_cps(self, item):
        """
        Get the current CPS of an item
        Will throw a KeyError exception if item is not in the build info.
        """
        return self._info[item][1]
    
    def update_item(self, item):
        """
        Update the cost of an item by the growth factor
        Will throw a KeyError exception if item is not in the build info.
        """
        cost, cps = self._info[item]
        self._info[item] = [cost * self._build_growth, cps]
        
    def clone(self):
        """
        Return a clone of this BuildInfo
        """
        return BuildInfo(self._info, self._build_growth)


'''
Cookie Clicker Simulator
'''
   
import math
import pylab
import random
#import simpleplot

# used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

#import poc_clicker_provided as provided


# constant
SIM_TIME = 10000000000.0


class ClickerState:
    '''
    simple class to keep track of the game state;
    also track the history as a list of tuples
    '''
    
    def __init__(self):
        # class is keeping track of four things
        self._total_amount_of_cookies = 0.0
        self._current_amount_of_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0
        # then keeping a history of the game:
        # a time, an item, the cost of that item, total number by that time
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        '''
        return human readable current state
        '''
        return 'total amount: ' + str('{0:.1f}'.format(self._total_amount_of_cookies)) + '\n' \
               'current amount: ' + str('{0:.1f}'.format(self._current_amount_of_cookies)) + '\n' \
               'current time: ' + str(self._current_time) + '\n' \
               'current CPS: ' + str(self._current_cps)
    
    def get_cookies(self):
        '''
        return current number of cookies (not total number of cookies);
        should return a float
        '''
        return self._current_amount_of_cookies
    
    def get_cps(self):
        '''
        get current CPS; should return a float
        '''
        return self._current_cps
    
    def get_time(self):
        '''
        get current time; should return a float
        '''
        return self._current_time
    
    def get_history(self):
        '''
        return history list;
        example, as initialized: (0.0, None, 0.0, 0.0)
        '''
        return self._history

    def time_until(self, cookies):
        '''
        return time until you have the given number of cookies
        (could be 0 if you already have enough cookies);
        should return a float with no fractional part
        '''
        if self._current_amount_of_cookies >= cookies:
            return 0.0
        else:
            # consider only the given number of cookies (without current resource)
            return math.ceil((cookies - self._current_amount_of_cookies) / self._current_cps)
    
    def wait(self, time):
        '''
        wait for given amount of time and update state;
        should do nothing if time <= 0
        '''
        if time <= 0:
            pass
        else:
            self._current_time += time
            self._current_amount_of_cookies += time * self._current_cps
            self._total_amount_of_cookies += time * self._current_cps
            
    def buy_item(self, item_name, cost, additional_cps):
        '''
        buy an item and update state;
        should do nothing if you cannot afford the item
        '''
        if cost > self._current_amount_of_cookies:
            pass
        else:
            self._current_amount_of_cookies -= cost
            self._current_cps += additional_cps
            self._history.append((self._current_time, item_name, cost,
                                 self._total_amount_of_cookies))  
  
    
def simulate_clicker(build_info, duration, strategy):
    '''
    function to run a Cookie Clicker game for the given duration with
    the given strategy;
    returns a ClickerState object corresponding to game
    '''
    # make a clone of the build_info object & create a new ClickerState object
    cloned_build_info = build_info.clone()
    new_click = ClickerState()

    while 0 <= duration:
        item = strategy(new_click.get_cookies(), new_click.get_cps(), 
                        duration, cloned_build_info)
        if item is None:
            # no resources anymore, no more items will be purchased
            break
        item_cost = cloned_build_info.get_cost(item)
        wait_time = new_click.time_until(item_cost)
        if duration < wait_time:
            # impossible, would have to wait until after the duration
            break
        else:
            duration -= wait_time
            new_click.wait(wait_time)
            new_click.buy_item(item, item_cost, cloned_build_info.get_cps(item))
            cloned_build_info.update_item(item)
    # if there is still time left, allow cookies to accumulate till the end
    new_click.wait(duration)
               
    return new_click
    

def strategy_cursor(cookies, cps, time_left, build_info):
    '''
    always pick Cursor!

    note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left;
    your strategy functions must do this and return None rather than
    an item you can't buy in the time left
    '''
    return 'Cursor'

def strategy_none(cookies, cps, time_left, build_info):
    '''
    always return None

    this is a pointless strategy that you can use to help debug
    your simulate_clicker function
    '''
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    '''
    always select the cheapest item that you can afford in the time left;
    not enough time left for you to buy any more items, return None
    '''
    inventory = {}
    name = None

    for item in build_info.build_items():
        inventory[item] = build_info.get_cost(item)
    cheapest = min(inventory.values())
    # still enough time left to buy at least one more item
    if cheapest <= (cookies + (time_left * cps)):
        # looking in the dictionary for a key to known minimal (cheapest) value
        for name, cost in inventory.items():
            if cost == cheapest:
                return name
    
def strategy_expensive(cookies, cps, time_left, build_info):
    '''
    always select the most expensive item you can afford in the time left
    not enough time left for you to buy any more items, return None
    '''
    # for extra exercise, different approach from the one used in strategy_cheap
    inventory = build_info.build_items()
    name = None
    most_expensive = float('-inf')
    resource = cookies + (time_left * cps)

    for item in inventory:
        current_cost = build_info.get_cost(item)
        # still enough time to buy at least one more (most expensive) item
        if current_cost <= resource and most_expensive < current_cost:
            # found currently most expensive item, store it temporarly
            most_expensive = current_cost
            name = item
    return name

def strategy_best(cookies, cps, time_left, build_info):
    '''
    approach to maximalize the production output based on 'fastest from zero cookies' idea at:
    http://www.reddit.com/r/CookieClicker/comments/1lsuov/yet_another_calculator_this_one_in_htmljavascript/cc3eqs7
    doesn't achieve high enough score as these:
    https://class.coursera.org/principlescomputing-001/forum/thread?thread_id=916
    '''
    inventory = build_info.build_items()
    cost_sorted_list = []
    name = None
    fastest_from_zero = float('-inf')
    resource = cookies + (time_left * cps)

    # to ease pointing at two items at once later on, created helper sorted list (by cost) 
    for item in inventory:
        cost_sorted_list.append([build_info.get_cost(item), item])
        cost_sorted_list.sort()

    for item in xrange(len(cost_sorted_list) - 1):
        item_a = cost_sorted_list[item][1]
        current_cost_a = build_info.get_cost(item_a)
        item_b = cost_sorted_list[item + 1][1]
        current_cost_b = build_info.get_cost(item_b)
        # still enough time to buy at least one from a pair of considered items
        if current_cost_a or current_cost_b <= resource:
            a = (current_cost_a / cps) + current_cost_b / (build_info.get_cps(item_a) + cps)
            b = (current_cost_b / cps) + current_cost_a / (build_info.get_cps(item_b) + cps)
            if fastest_from_zero < a and b:
                # found currently 'fastest from zero cookies' item, store it temporarly
                if a < b:
                    fastest_from_zero = a
                    name = item_a
                else:
                    fastest_from_zero = b
                    name = item_b
    return name
    
    # TODO by k., possible follow up at: http://code.google.com/codejam/contest/2974486/dashboard#s=p1
    
def strategy_random(cookies, cps, time_left, build_info):
    '''
    my own approach to get close enough to maximalize the production output
    '''
    # aka Entropy beats everything in long term!
    return random.choice(build_info.build_items())

       
def run_strategy(strategy_name, time, strategy):
    '''
    run a simulation with one strategy
    '''
    #state = simulate_clicker(provided.BuildInfo(), time, strategy)
    # removed 'provided' in order to make it run in IDLE
    state = simulate_clicker(BuildInfo(), time, strategy)
    print strategy_name, ':', state, '\n\n', 'Plotting a graph, wait please...'

    history = state.get_history()
    time = [item[0] for item in history]
    cookies = [item[3] for item in history]
    cost = [item[2] for item in history]
    
    # plot in pylab (total cookies over time / cost of the item)
    pylab.plot(time, cookies, 'o', color = 'brown')
    pylab.plot(time, cost)
    pylab.title(strategy_name + ' Strategy')
    pylab.legend(('Total Amount of Cookies', 'Item Cost'))
    pylab.xlabel('Time')
    pylab.ylabel('Amount / Cost Value')
    pylab.show()

    
    # plot in silly simpleplot from the class (total cookies over time)
    # uncomment out the lines below to see a plot of total cookies vs. time;
    # be sure to allow popups in browser, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)


def run():
    '''
    run the simulator
    '''    
    #run_strategy('Cursor', SIM_TIME, strategy_cursor)

    # add calls to run_strategy to run additional strategies
    run_strategy('Cheap', SIM_TIME, strategy_cheap)
    run_strategy('Expensive', SIM_TIME, strategy_expensive)
    run_strategy('Best', SIM_TIME, strategy_best)
    run_strategy('Random Pick', SIM_TIME, strategy_random)

# let's run it!
run()
