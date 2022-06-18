from pprint import pprint

file_name = 'cook_book.txt'

def cook_book_dict(file_name):
    with open(file_name) as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredients = []
            for item in range(int(file.readline())):
                ingredient_name = 'ingredient_name'
                quantity = 'quantity'
                measure = 'measure'
                ingredient = file.readline().strip().split(' | ')
                ingredient_unit = dict(ingredient_name = ingredient[0], quantity = int(ingredient[1]),  measure = ingredient[2])
                ingredients.append(ingredient_unit)
            file.readline()
            cook_book[dish_name] = ingredients
        return cook_book


result = cook_book_dict(file_name)
pprint(result)

