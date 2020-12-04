
def part1(inputs):
    '''
    From your starting position at the top-left, check the position
    that is right 3 and down 1. Then, check the position that
    is right 3 and down 1 from there, and so on until you go past the bottom of the map.
    '''

    pos = (0, 0)
    slope = (3, 1)
    trees = 0
    length = len(inputs[0])
    pos = (pos[0] + slope[0], pos[1] + slope[1])
    while pos[1] < len(inputs):
        if inputs[pos[1]][pos[0] % length] == '#':
            trees += 1
        pos = (pos[0] + slope[0], pos[1] + slope[1])
    return trees


def part2(inputs):
    '''
    Determine the number of trees you would encounter if, for each
    of the following slopes, you start at the top-left corner and
    traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

    In the above example, these slopes would find 2, 7, 3, 4, and 2
    tree(s) respectively; multiplied together, these produce the answer 336.

    What do you get if you multiply together the number of trees encountered
    on each of the listed slopes?
    '''

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total_trees = 1
    for slope in slopes:
        trees = 0
        pos = (0, 0)
        length = len(inputs[0])
        pos = (pos[0] + slope[0], pos[1] + slope[1])
        while pos[1] < len(inputs):
            if inputs[pos[1]][pos[0] % length] == '#':
                trees += 1
            pos = (pos[0] + slope[0], pos[1] + slope[1])
        total_trees *= trees
    return total_trees
