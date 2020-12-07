import re
import logging

logger = logging.getLogger('AOC2020')
entry = '  [-]'

def parse_passport(input_line):
    '''
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    '''

    byr = re.compile(r'byr:(?:19[2-9][0-9]|200[0-2])\s')
    iyr = re.compile(r'iyr:20(?:1[0-9]|20)\s')
    eyr = re.compile(r'eyr:20(?:2[0-9]|30)\s')
    hgt = re.compile(r'hgt:(?:(?:(?:1[5-8][0-9]|19[0-3])cm)|(?:(?:59|6[0-9]|7[0-6])in))\s')
    # hgt = re.compile(r'hgt:')
    hcl = re.compile(r'hcl:#[0-9a-f]{6}\s')
    ecl = re.compile(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)\s')
    pid = re.compile(r'pid:\d{9}\s')
    cid = re.compile(r'cid:\S+')
    required = [byr, iyr, eyr, hgt,
                hcl, ecl, pid]
    optional = [cid]
    value = '    [+]'
    logger.debug(f'{entry} Input: {input_line}')
    for pattern in required:
        logger.debug(f'{value} Pattern: {pattern}')
        if match := pattern.search(input_line) is None:
            logger.debug(f'{value} -- Failed')
            return False
        logger.debug(f'{value} -- Success')
    return True

def part1(inputs):
    '''
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID) - optional

    Count the number of valid passports - those that have all
    required fields. Treat cid as optional. In your batch file,
    how many passports are valid?
    '''
    # logger.debug(f'{entry} Inputs: {inputs}')
    # passports = list(''.join(inputs).split('\n'))
    passports = []
    passport = ''
    for input_line in inputs:
        if input_line == '':
            passports.append(passport.strip() + ' ')
            passport = ''
        else:
            passport += f' {input_line}'
    passports.append(passport)
    # logger.debug(f'{entry} Passports: {passports}')
    valid_passports = list(filter(parse_passport, passports))
    # logger.debug(f'{entry} Valid: {valid_passports}')
    return len(valid_passports)


def part2(inputs):
    '''
    You can continue to ignore the cid field, but each other field has
     strict rules about what values are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

    Your job is to count the passports where all required fields are both
    present and valid according to the above rules.
    '''
    logger.debug(f'{entry} Inputs: {len(inputs)}')
    # passports = list(''.join(inputs).split('\n'))
    passports = []
    passport = ''
    for input_line in inputs:
        if input_line == '':
            passports.append(passport.strip() + ' ')
            passport = ''
        else:
            passport += f' {input_line}'
    passports.append(passport + ' ')
    logger.debug(f'{entry} Passports: {len(passports)}')
    valid_passports = list(filter(parse_passport, passports))
    with open('valid_passports.txt', 'w') as f:
        f.write('\n'.join(valid_passports))
    # logger.debug(f'{entry} Valid: {valid_passports}')
    return len(valid_passports)