total_allergens = set()

inputs = []

with open('puzzle_inputs.txt') as f:
    for line in f:
        line = line.replace('\n', '')
        split = line.split('(')
        ingredients = split[0].strip().split(' ')
        allergens = split[1].replace('contains', '').replace(')', '').replace(' ', '').split(',')

        inputs.append({
            'food': ingredients,
            'allergens': allergens
        })

        total_allergens.update(allergens)


def food_containing_allergen(allergen, inputs):
    foods = []

    for input in inputs:
        if allergen in input['allergens']:
            foods.append(input['food'])

    return foods


def present_in_all_lists(item, lists):
    for lst in lists:
        if item not in lst:
            return False

    return True


def remove_allergen(allergen, inputs):
    for input in inputs:
        if allergen in input['allergens']:
            input['allergens'].remove(allergen)


def remove_ingredient(ingredient, inputs):
    for input in inputs:
        if ingredient in input['food']:
            input['food'].remove(ingredient)


def find_solutions(inputs, total_allergens):
    allergen_ingredient = {}

    while len(allergen_ingredient) != len(total_allergens):
        for input in inputs:
            ingredients = input['food']
            allergens = input['allergens']

            if len(allergens) == 1:
                foods = food_containing_allergen(allergens[0], inputs)
                for ingredient in ingredients:
                    if present_in_all_lists(ingredient, foods):
                        allergen_ingredient[allergens[0]] = ingredient
                        remove_ingredient(ingredient, inputs)
                        remove_allergen(allergens[0], inputs)
                        break

    answer1 = sum([len(input['food']) for input in inputs])

    allergens = list(allergen_ingredient.keys())
    allergens.sort()

    answer2 = ''

    for allergen in allergens:
        answer2 += allergen_ingredient[allergen] + ','

    return answer1, answer2[:-1]


answer1, answer2 = find_solutions(inputs, total_allergens)

print('Part One Solution:', answer1)
print('Part Two Solution:', answer2)
