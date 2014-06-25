# Homework 1 for Principles of Computing class, by k., 06/24/2014

import math
import pylab
#import simpleplot
#import codeskulptor
#codeskulptor.set_timeout(20)


# Question 1

'''
Simulator for resource generation with upgrades
'''

def resources_vs_time(upgrade_cost_increment, num_upgrade):
    '''
    build function that performs unit upgrades with specified cost increments;
    return a list whose length is num_upgrades and whose entries are pairs of the form:
    [current_time, total_resources_generated]
    '''
    resources = []
    total_resources_generated = 0.0
    current_time = 0.0
    current_resources = 1.0
    growth = 1.0
    
    for item in xrange(num_upgrade):
        current_time += current_resources / growth # incremental time to achieve upgrade
        total_resources_generated += growth * (current_resources / growth)
        current_resources += upgrade_cost_increment
        growth += 1
        resources.append([current_time, total_resources_generated])
        
    return resources

# sample output from the print statements for data1 and data2
#[[1.0, 1], [1.75, 2.5], [2.41666666667, 4.5], [3.04166666667, 7.0], [3.64166666667, 10.0], [4.225, 13.5], [4.79642857143, 17.5], [5.35892857143, 22.0], [5.91448412698, 27.0], [6.46448412698, 32.5], [7.00993867244, 38.5], [7.55160533911, 45.0], [8.09006687757, 52.0], [8.62578116328, 59.5], [9.15911449661, 67.5], [9.69036449661, 76.0], [10.2197762613, 85.0], [10.7475540391, 94.5], [11.2738698286, 104.5], [11.7988698286, 115.0]]
#[[1.0, 1], [2.25, 3.5], [3.58333333333, 7.5], [4.95833333333, 13.0], [6.35833333333, 20.0], [7.775, 28.5], [9.20357142857, 38.5], [10.6410714286, 50.0], [12.085515873, 63.0], [13.535515873, 77.5]]

# quick test
#print resources_vs_time(0.5, 20)
#print resources_vs_time(1.5, 10)

# results for question
#print resources_vs_time(0.0, 10)
#print
#print resources_vs_time(1.0, 10)

def plot_it():
    '''
    helper function to gain insight on provided data sets background,
    using pylab
    '''
    data1 = [[1.0, 1], [2.25, 3.5], [3.58333333333, 7.5], [4.95833333333, 13.0], [6.35833333333, 20.0], [7.775, 28.5], [9.20357142857, 38.5], [10.6410714286, 50.0], [12.085515873, 63.0], [13.535515873, 77.5]]
    data2 = [[1.0, 1], [1.75, 2.5], [2.41666666667, 4.5], [3.04166666667, 7.0], [3.64166666667, 10.0], [4.225, 13.5], [4.79642857143, 17.5], [5.35892857143, 22.0], [5.91448412698, 27.0], [6.46448412698, 32.5], [7.00993867244, 38.5], [7.55160533911, 45.0], [8.09006687757, 52.0], [8.62578116328, 59.5], [9.15911449661, 67.5], [9.69036449661, 76.0], [10.2197762613, 85.0], [10.7475540391, 94.5], [11.2738698286, 104.5], [11.7988698286, 115.0]]
    time1 = [item[0] for item in data1]
    resource1 = [item[1] for item in data1]
    time2 = [item[0] for item in data2]
    resource2 = [item[1] for item in data2]
    
    # plot in pylab (total resources over time)
    pylab.plot(time1, resource1, 'o')
    pylab.plot(time2, resource2, 'o')
    pylab.title('Silly Homework')
    pylab.legend(('Data Set no.1', 'Data Set no.2'))
    pylab.xlabel('Current Time')
    pylab.ylabel('Total Resources Generated')
    pylab.show()

#plot_it()    

def test():
    '''
    testing code for resources_vs_time,
    '''
    data1 = resources_vs_time(0.5, 20)
    data2 = resources_vs_time(1.5, 10)
    print data1
    print data2
    simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [data1, data2])

# using silly simpleplot from the class, don't bother!
#test()


# Question 2

def plot_question2():
    '''
    graph of total resources generated as a function of time,
    for four various upgrade_cost_increment values
    '''
    for upgrade_cost_increment in [0.0, 0.5, 1.0, 2.0]:
        data = resources_vs_time(upgrade_cost_increment, 5)
        time = [item[0] for item in data]
        resource = [item[1] for item in data]
    
        # plot in pylab (total resources over time for each constant)
        pylab.plot(time, resource, 'o')
        
    pylab.title('Silly Homework')
    pylab.legend(('0.0', '0.5', '1.0', '2.0'))
    pylab.xlabel('Current Time')
    pylab.ylabel('Total Resources Generated')
    pylab.show()

#plot_question2()   


# Question 3

def plot_question3():
    '''
    graph of total resources generated as a function of time;
    for upgrade_cost_increment == 0
    '''
    data = resources_vs_time(0.0, 100)
    time = [item[0] for item in data]
    resource = [item[1] for item in data]

    # plot in pylab on logarithmic scale (total resources over time for upgrade growth 0.0)
    pylab.loglog(time, resource)
        
    pylab.title('Silly Homework')
    pylab.legend('0.0')
    pylab.xlabel('Current Time')
    pylab.ylabel('Total Resources Generated')
    pylab.show()

#plot_question3()


# Question 4

def arithmetic_sum_model():
    '''
    find what arithmetic sum models the value of current_time after n upgrades,
    for upgrade_cost_increment == 0
    '''
    print 'Incremental time to achieve upgrade / Incremental resources'
    data = resources_vs_time(0.0, 10)
    time = [item[0] for item in data]
    resource = [item[1] for item in data]
    for index in xrange(len(time) - 1):
        delta1 = time[index + 1] - time[index]
        delta2 = resource[index + 1] - resource[index]
        print delta1, '\t', delta2
           
#arithmetic_sum_model()


# Question 5

def total_sum_model():
    '''
    find what function f(n) models the total value of the sum most accurately,
    for upgrade_cost_increment == 0
    '''
    num_upgrade = 1000.0
    deltas = []
    
    data = resources_vs_time(0.0, int(num_upgrade))
    resource = [item[0] for item in data]
    for index in xrange(len(resource) - 1):
        deltas.append(resource[index + 1] - resource[index])

    print 'n number of upgrades: ', num_upgrade
    print 'Note that number in question will differ by a small constant as grows large.'
    print 'The total value of the sum: ', sum(deltas)
    print 'Modeled value (1/2n(n+1)) of the sum: ', 1.0 / 2 * num_upgrade * (num_upgrade + 1.0)
    print 'Modeled value (n) of the sum: ', num_upgrade
    print 'Modeled value (2) of the sum: ', 2.0
    print 'Modeled value (log(n)) of the sum: ', math.log10(num_upgrade)

#total_sum_model()


# Question 6

def time_upgrades_relationship_0():
    '''
    helper function to show relationship between time and number of upgrades,
    for upgrade_cost_increment == 0.0
    '''
    print 'Incremental time to achieve upgrade'
    data = resources_vs_time(0.0, 11)
    time = [item[0] for item in data]
    resource = [item[1] for item in data]
    for index in xrange(len(time) - 1):
        delta1 = time[index + 1] - time[index]
        delta2 = resource[index + 1] - resource[index]
        print delta1, '\t\t', delta2
    print '\nsum is called a harmonic sum and has only an approximate solution: log(t) + constant;'
    print 'question 6 asks for "...we seek the inverse function g for f..." thus e**(t) in form E^t'

#time_upgrades_relationship_0()


# Question 7

def polyfitting():
    '''
    helper function to play around with polyfit from:
    http://www.wired.com/2011/01/linear-regression-with-pylab/
    '''
    x = [0.2, 1.3, 2.1, 2.9, 3.3]
    y = [3.3, 3.9, 4.8, 5.5, 6.9]
    slope, intercept = pylab.polyfit(x, y, 1)
    print 'slope:', slope, 'intercept:', intercept

    yp = pylab.polyval([slope, intercept], x)
    pylab.plot(x, yp)
    pylab.scatter(x, y)
    pylab.show()

#polyfitting()

def fitting_easy():
    '''
    helper function to check slot, the slope is 4.0
    '''
    x = [0.0, 7.0, 14.0]
    y = [0.0, 28.0, 56.0]
    print round((y[1] - y[0]) / (x[1] - x[0]))

#fitting_easy()
    
def plot_question7():
    '''
    graph of total resources generated as a function of time,
    for upgrade_cost_increment == 1
    '''
    data = resources_vs_time(1.0, 50)
    time = [item[0] for item in data]
    resource = [item[1] for item in data]
    a, b, c = pylab.polyfit(time, resource, 2)
    print 'polyfit with argument \'2\' fits the data, thus the degree of the polynomial is 2 (quadratic)'

    # plot in pylab on logarithmic scale (total resources over time for upgrade growth 0.0)
    #pylab.loglog(time, resource, 'o')

    # plot fitting function
    yp = pylab.polyval([a, b, c], time)
    pylab.plot(time, yp)
    pylab.scatter(time, resource)
    pylab.title('Silly Homework, Question 7')
    pylab.legend(('Resources for increment 1', 'Fitting function' + ', slope: ' + str(a)))
    pylab.xlabel('Current Time')
    pylab.ylabel('Total Resources Generated')
    pylab.grid()
    pylab.show()

plot_question7()


# Question 8

def arithmetic_sum_model_resources():
    '''
    find what arithmetic sum models the value of current_time after n upgrades,
    for upgrade_cost_increment == 1.0
    '''
    print 'Incremental time to achieve upgrade / Incremental resources'
    data = resources_vs_time(1.0, 10)
    time = [item[0] for item in data]
    resource = [item[1] for item in data]
    for index in xrange(len(time) - 1):
        delta1 = time[index + 1] - time[index]
        delta2 = resource[index + 1] - resource[index]
        print delta1, '\t', delta2
           
#arithmetic_sum_model_resources()


# Question 9

def time_upgrades_relationship():
    '''
    helper function to show relationship between time and number of upgrades,
    for upgrade_cost_increment == 1.0
    '''
    print 'Time unit / Incremental resources'
    data = resources_vs_time(1.0, 10)
    time = [item[0] for item in data]
    resource = [item[1] for item in data]
    for index in xrange(len(time) - 1):
        delta = resource[index + 1] - resource[index]
        print time[index], '\t', delta
    print 'sum is known as a triangular sum, 1/2(n + 1)n; for t it\'s 1/2(t + 1)t'    

#time_upgrades_relationship()

    
# Question 10

def upgrade_cost(number):
    '''
    helper function for expression that models the cost of the nth upgrade
    '''
    accumulator = []
    for number in xrange(1, number + 1):
        cost = 1.15 ** (number - 1)
        accumulator.append([number, cost])
    return accumulator

#print upgrade_cost(10)


# Question 11

def plot_question11():
    '''
    graph of total resources generated as a function of time;
    for upgrade_cost_increment == 1
    '''
    num_upgrade = 10.0
    # function from question 1
    data1 = resources_vs_time(1.0, int(num_upgrade))
    time1 = [item[0] for item in data1]
    resource1 = [item[1] for item in data1]
    # function from question 10
    data2 = upgrade_cost(int(num_upgrade))
    time2 = [item[0] for item in data2]
    resource2 = [item[1] for item in data2]
   
    # plot in pylab (to see how fast both functions grow)
    pylab.plot(time1, resource1)
    pylab.plot(time2, resource2)
        
    pylab.title('Silly Homework')
    pylab.legend(('quadratic function of time', 'upgrade costs 15% more'))
    pylab.xlabel('Current Time')
    pylab.ylabel('Total Resources Generated')
    pylab.show()

#plot_question11()
