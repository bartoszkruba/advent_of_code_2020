import re

inputs = []

with open('puzzle_inputs.txt') as f:
    for line in f:
        inputs.append(line.replace("\n", ""))


def parse_passports(inputs):
    passports = []

    currentPassport = {}

    for input in inputs:
        if len(input) == 0:
            passports.append(currentPassport)
            currentPassport = {}
        else:
            for item in input.split(' '):
                currentPassport[item.split(":")[0]] = item.split(":")[1]
    passports.append(currentPassport)
    return passports


def filter_passwords(passports, rules):
    def filter_fun(passport):
        for field in rules:
            if field not in passport:
                return False
            for rule in rules[field]:
                if rule == 'length' and len(passport[field]) != rules[field][rule]:
                    return False
                if rule == 'min' and int(passport[field]) < rules[field][rule]:
                    return False
                if rule == 'max' and int(passport[field]) > rules[field][rule]:
                    return False
                if rule == 'regex' and re.compile(str(rules[field][rule])).match(passport[field]) is None:
                    return False
                if rule == 'in' and passport[field] not in rules[field][rule]:
                    return False
                if rule == 'custom' and rules[field][rule](passport[field]) is False:
                    return False
        return True

    return list(filter(filter_fun, passports))


def find_solution1(passports):
    rules = {'byr': {}, 'iyr': {}, 'eyr': {}, 'hgt': {}, 'hcl': {}, 'ecl': {}, 'pid': {}}

    return len(filter_passwords(passports, rules))


passports = parse_passports(inputs)
print("Part one solution: ", find_solution1(passports))


def find_solution2(passports):
    rules = {
        'byr': {
            'length': 4,
            'min': 1920,
            'max': 2002
        },
        'iyr': {
            'length': 4,
            'min': 2010,
            'max': 2020
        },
        'eyr': {
            'length': 4,
            'min': 2020,
            'max': 2030
        },
        'hgt': {
            'regex': '^[0-9]{3}cm|[0-9]{2}in$',
            'custom': lambda x: (150 <= int(x[:-2]) <= 193) if x[-2:] == 'cm' else (59 <= int(x[:-2]) <= 76)
        },
        'hcl': {
            'regex': '^#[0-9a-f]{6}$'
        },
        'ecl': {
            'in': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        },
        'pid': {
            'regex': '^[0-9]{9}$'
        }
    }

    return len(filter_passwords(passports, rules))


print("Part two solution: ", find_solution2(passports))
