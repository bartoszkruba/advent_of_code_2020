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


def find_solution1(passports):
    def passport_is_valid(passport):
        for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if key not in passport:
                return False
        return True

    return len(list(filter(passport_is_valid, passports)))


passports = parse_passports(inputs)
print("Part one solution: ", find_solution1(passports))
