def add_pairs(input_list):
    for i, item in enumerate(input_list):
        for j in range(i+1, len(input_list)):
            yield [input_list[i], input_list[j]]

def add_triplets(input_list):
    for i, item in enumerate(input_list):
        for j in range(i+1, len(input_list)):
            for k in range(i+2, len(input_list)):
                yield [input_list[i], input_list[j], input_list[k]]

def part1(inputs):
    '''
    Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

    Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

    For example, suppose your expense report contained the following:

    1721
    979
    366
    299
    675
    1456

    In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
    '''

    inputs = [int(input) for input in inputs]
    for result in add_pairs(inputs):
        if sum(result) == 2020:
            return result[0] * result[1]

def part2(inputs):
    '''
    The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

    Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

    In your expense report, what is the product of the three entries that sum to 2020?
    '''
    inputs = [int(input) for input in inputs]
    for result in add_triplets(inputs):
        if sum(result) == 2020:
            return result[0] * result[1] * result[2]
