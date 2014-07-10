# Practice Activity 4 for Principles of Computing class, by k., 07/10/2014
# Working with Distance Fields (see https://class.coursera.org/principlescomputing-001/wiki/view?page=distance_fields )
# skeleton code: http://www.codeskulptor.org/#poc_distance_template.py
# official solution: http://www.codeskulptor.org/#poc_distance_solution.py


'''
an example of creating a distance field using Manhattan distance
'''

GRID_HEIGHT = 6
GRID_WIDTH = 8

def manhattan_distance(row0, col0, row1, col1):
    '''
    compute the Manhattan distance between the cells (row0, col0) and (row1, col1)
    '''
    return abs(row0 - row1) + abs(col0 - col1)

        
def create_distance_field(entity_list):
    '''
    create a Manhattan distance field that contains the minimum distance to 
    each entity (zombies or humans) in entity_list;
    each entity is represented as a grid position of the form (row, col) 
    '''
    individual_distances = []
    for entity in entity_list:
        row, col = entity
        # for each entity, add a list of distances in regards to this entity
        individual_distances.append([manhattan_distance(x, y, row, col) for x in range(GRID_HEIGHT) for y in range(GRID_WIDTH)])
    # project all distances onto each other (get minimum value for each cell from unzipped lists)
    combined_distances = map(min, zip(*individual_distances))

    # organize output in single row fashion (apparently expected from this function) 
    return [combined_distances[i:i + GRID_WIDTH] for i in range(0, len(combined_distances), GRID_WIDTH)]


def print_field(field):
    '''
    print a distance field in a human readable manner with one row per line
    '''
    for item in field:
        print item    


def run_example():
    '''
    create and print a small distance field
    '''    
    field = create_distance_field([[4, 0],[2, 5]])
    print_field(field)
    
#run_example()


# Sample output for the default example
#[4, 5, 5, 4, 3, 2, 3, 4]
#[3, 4, 4, 3, 2, 1, 2, 3]
#[2, 3, 3, 2, 1, 0, 1, 2]
#[1, 2, 3, 3, 2, 1, 2, 3]
#[0, 1, 2, 3, 3, 2, 3, 4]
#[1, 2, 3, 4, 4, 3, 4, 5]
