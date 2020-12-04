from collections import Counter

def parse_line(line):
    pieces = line.split()
    min_val, max_val = pieces[0].split('-')
    return (
        int(min_val),
        int(max_val),
        pieces[1].replace(':', ''),
        pieces[2]
    )

def part1(inputs):
    '''
    To try to debug the problem, they have created a list (your puzzle input)
    of passwords (according to the corrupted database)
    and the corporate policy when that password was set.

    Each line gives the password policy and then the password.
     The password policy indicates the lowest and highest number of times a
     given letter must appear for the password to be valid. For example,
     1-3 a means that the password must contain a at least 1 time and at most 3 times.

    In the above example, 2 passwords are valid. The middle password, cdefg,
    is not; it contains no instances of b, but needs at least 1.
    The first and third passwords are valid: they contain one a or nine c,
    both within the limits of their respective policies.

    How many passwords are valid according to their policies?
    '''

    valid_passwords = 0

    for line in inputs:
        min_val, max_val, letter, password = parse_line(line)
        counts = Counter(password)
        letter_count = counts[letter]
        if min_val <= letter_count <= max_val:
            valid_passwords += 1
    return valid_passwords


def part2(inputs):
    '''
    Each policy actually describes two positions in the password, where 1 means
     the first character, 2 means the second character, and so on.
     (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
     Exactly one of these positions must contain the given letter.
     Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

    Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

    How many passwords are valid according to the new interpretation of the policies?
    '''

    valid_passwords = 0
    for line in inputs:
        pos1, pos2, letter, password = parse_line(line)
        letters = password[pos1-1] + password[pos2-1]
        counts = Counter(letters)
        if counts[letter] == 1:
            valid_passwords += 1
    return valid_passwords