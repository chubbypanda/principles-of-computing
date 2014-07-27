# Homework 6 for Principles of Computing class, by k., 07/26/2014

class Incrementer(object):
    '''
    counting increments separately from the function
    '''
    def __init__(self, count):
        self.count = count

    def increment(self):
        self.count += 1


'''
basic Tree class

IMPORTANT:  Some class methods assume that instances of the Tree class
always have a single parent (or no parent for the root). See problem #8
on homework #6 for more details.
'''

class Tree:
    """
    Recursive definition for trees plus various tree methods
    """
    
    def __init__(self, value, children):
        """
        Create a tree whose root has specific value (a string)
        Children is a list of references to the roots of the subtrees.  
        """
        
        self._value = value
        self._children = children
        
        
    def __str__(self):
        """
        Generate a string representation of the tree
        Use an pre-order traversal of the tree
        """
        
        ans = "["
        ans += str(self._value)
                   
        for child in self._children:
             ans += ", "
             ans += str(child)
        return ans + "]"

    def get_value(self):
        """
        Getter for node's value
        """
        return self._value

    def children(self):
        """
        Generator to return children
        """
        for child in self._children:
            yield child
                    
    def num_nodes(self):
        """
        Compute number of nodes in the tree
        """
        ans = 1
        for child in self._children:
            ans += child.num_nodes()
        return ans
    
    def num_leaves(self):
        """
        Count number of leaves in tree
        """
        if len(self._children) == 0:
            return 1
        
        ans = 0
        for child in self._children:
            ans += child.num_leaves()
        return ans

    def height(self):
        """
        Compute height of a tree rooted by self
        """
        height = 0
        for child in self._children:
            height = max(height, child.height() + 1)
        return height


# Question 1

'''
recursive class definition for a non-empty list of nodes
'''

class NodeList:
    '''
    class definition for non-empty lists using recursion
    '''
    def __init__(self, val):
        '''
        create a list with one node
        '''
        self._value = val
        self._next = None
         
    def append(self, val):
        '''
        append a node to an existing list of nodes
        '''
        i.increment()
        if self._next == None:
            new_node = NodeList(val)
            self._next = new_node
        else:
            self._next.append(val)
           
    def __str__(self):
        '''
        build standard string representation for list
        '''
        if self._next == None:
            return '[' + str(self._value) + ']'
        else:
            rest_str = str(self._next)
            rest_str = rest_str[1 :]
            return '[' + str(self._value) + ', ' + rest_str
    
def run_example():
    '''
    create some examples
    '''
    node_list = NodeList(2)
    node_list.append(3)
    node_list.append(4)
    print node_list
    
    sub_list = NodeList(5)
    sub_list.append(6)
    
    node_list.append(sub_list)
    print node_list
    
#run_example()
test = NodeList(2)
print 'Question 1 answer:', type(test._next)             

        
# Question 2

print '\nPrep for Question 2 follows...'
i = Incrementer(0)
test = NodeList(10)
print 'when n is 0:', i.count
test.append(1)
print 'when n is 1:', i.count - 0
test.append(2)
print 'when n is 2:', i.count - 1
test.append(3)
print 'when n is 3:', i.count - 3
test.append(45)
print 'when n is 4:', i.count - 6
test.append(6)
print 'when n is 5:', i.count - 10
test.append(9)
print 'when n is 6:', i.count - 15
test.append(100)
print 'when n is 7:', i.count - 21


# Questions 3 and 4

'''
navigable Tree class
'''

class NavTree(Tree):
    '''
    recursive definition for navigable trees plus extra tree methods
    '''
    def __init__(self, value, children, parent = None):
        '''
        create a tree whose root has specific value (a string)
        children is a list of references to the roots of the children;  
        parent (if specified) is a reference to the tree's parent node
        '''
        
        Tree.__init__(self, value, children)
        self._parent = parent
        for child in self._children:
            child._parent = self          
    
    def set_parent(self, parent):
        '''
        update parent field
        '''
        self._parent = parent    
            
    def get_root(self):
        '''
        return the root of the tree
        '''
        if self._parent is None:
            return self
        else:
            return self._parent.get_root()

    def depth(self):
        '''
        return the depth of the self with respect to the root of the tree
        '''
        if self._parent is None:
            return 0
        else:
            return self._parent.depth() + 1
    
def run_examples3():
    '''
    Create some trees and apply various methods to these trees
    '''
    tree_a = NavTree('a', [])
    tree_b = NavTree('b', [])
    tree_cab = NavTree('c', [tree_a, tree_b]) 
    tree_e = NavTree('e', [])
    tree_dcabe = NavTree('d', [tree_cab, tree_e])
    
    print 'This is the main tree -', tree_dcabe
    print 'This is tree that contains b -', tree_b.get_root()
    
    #import poc_draw_tree
    #poc_draw_tree.TreeDisplay(tree_dcabe)

    print 'The node b has depth', tree_b.depth()
    print 'The node e has depth', tree_e.depth()

print '\nQuestion 3 passes.',
print '\nQuestion 4 passes.\n',        
run_examples3()

# Expect output
#This is the main tree - [d, [c, [a], [b]], [e]]]
#This is tree that contains b - [d, [c, [a], [b]], [e]]
#The node b has depth 2
#The node e has depth 1


# Question 5

print '\nPrep for Question 5 follows...'
print 'when n is 0:', 0
print 'when n is 1:', 1
print 'when n is 2:', 2 * 2 * 1
print 'when n is 3:', 2 * 2 * 2
print 'when n is 4:', 2 * 2 * 2 * 2
print 'when n is 5:', 2 * 2 * 2 * 2 * 2


# Question 6

print '\nPrep for Question 6 follows...'
print 'when n is 0:', 0
print 'when n is 1:', 1
print 'when n is 2:', 2**1 + (1)
print 'when n is 3:', 2**2 + (2**1 + 1)
print 'when n is 4:', 2**3 + (2**2 + 2**1 + 1)
print 'when n is 5:', 2**4 + (2**3 + 2**2 + 2**1 + 1)


# Question 7

print '\nQuestion 7 answer:', 4**1 + 4**2 + 4**3


# Question 8

def run_examples8():
    '''
    create some trees and apply various methods to these trees
    '''
    tree_PIII = Tree("Philip III", [])
    tree_MGA = Tree("Marganita, Aus", [])
    tree_PIV = Tree("Phillip IV", [tree_MGA, tree_PIII])
    tree_MAS = Tree("Maria Anna, Sp", [tree_PIII, tree_MGA])
    tree_FIII = Tree("Ferdinand III", [])
    tree_MA = Tree("Mariana, Aus", [tree_FIII, tree_MAS])
    tree_CII = Tree("Charles II", [tree_PIV, tree_MA])

    tree_PIII_hypo = Tree("Philip III", [])
    tree_MGA_hypo = Tree("Marganita, Aus", [])
    tree_PIV_hypo = Tree("Phillip IV", [tree_MGA_hypo, tree_PIII_hypo])
    tree_MAS_hypo = Tree("Maria Anna, Sp", [tree_PIII_hypo, tree_MGA_hypo])
    tree_FIII_hypo = Tree("Ferdinand III", [])
    tree_proper_father = Tree('Proper wife\' father', [])
    tree_FIII_proper = Tree('Ferdinand III\'s proper wife', [tree_proper_father])
    tree_MA_hypo = Tree('Mariana, Aus', [tree_FIII_hypo, tree_FIII_proper])
    tree_CII_hypo = Tree('Charles II', [tree_PIV_hypo, tree_MA_hypo])

    print '\nPrep for Question 8 follows...'
    print 'This is part of family tree:', tree_CII
    print 'This is part of hypothetical family tree:', tree_CII_hypo
    print 'Family tree values. Height:', tree_CII.height(), ', children:', len(tree_CII._children), \
          ', nodes:', tree_CII.num_nodes(), ', leaves:', tree_CII.num_leaves()
    print 'Hypothetical family tree values. Height:', tree_CII_hypo.height(), ', children:', len(tree_CII_hypo._children), \
          ', nodes:', tree_CII_hypo.num_nodes(), ', leaves:', tree_CII_hypo.num_leaves()
    
    #import poc_draw_tree
    #poc_draw_tree.TreeDisplay(my_tree)
            
run_examples8()


# Question 9

class modTree(Tree):
    def __str__(self):
        '''
        generate a string representation of the tree;
        modified version according to Question 9
        '''
        
        ans = '['
                   
        for child in self._children:
            ans += str(child)
            ans += ', '
        ans += str(self._value)

        return ans + ']'
    
    
def run_examples9():
    '''
    create some trees and apply various methods to these trees
    '''
##    tree_a = Tree("a", [])
##    tree_b = Tree("b", [])
##    print "Tree consisting of single leaf node labelled 'a'", tree_a
##    print "Tree consisting of single leaf node labelled 'b'", tree_b
##    
##    tree_cab = Tree("c", [tree_a, tree_b])
##    print "Tree consisting of three node", tree_cab
##    
##    tree_dcabe = Tree("d", [tree_cab, Tree("e", [])])
##    print "Tree consisting of five nodes", tree_dcabe
##    print 
##    
##    my_tree = Tree("a", [Tree("b", [Tree("c", []), Tree("d", [])]), 
##                         Tree("e", [Tree("f", [Tree("g", [])]), Tree("h", []), Tree("i", [])])])
##    print "Tree with nine nodes", my_tree
##    
##    print "The tree has", my_tree.num_nodes(), "nodes,", 
##    print my_tree.num_leaves(), "leaves and height",
##    print my_tree.height()
    question9_tree = Tree('d', [Tree('c', [Tree('a', []), Tree('b', [])]), Tree('e', [])])
    print '\nOriginal Question 9 representation:', question9_tree
    question9_mod_tree = modTree('d', [Tree('c', [Tree('a', []), Tree('b', [])]), Tree('e', [])])
    print 'Question 9 answer:', question9_mod_tree
    
    #import poc_draw_tree
    #poc_draw_tree.TreeDisplay(my_tree)
            
run_examples9()
