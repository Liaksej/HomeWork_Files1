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
                ingredient_unit = dict(ingredient_name = ingredient[0], quantity = int(ingredient[1]),
                                       measure = ingredient[2])
                ingredients.append(ingredient_unit)
            file.readline()
            cook_book[dish_name] = ingredients
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dict = {}
    for item in dishes:
        if item in cook_book_dict(file_name).keys():
            for dish, ingredients in cook_book_dict(file_name).items():
                if dish == item:
                    for ingredient in ingredients:
                        ingredient_name = ingredient['ingredient_name']
                        measure_value = ingredient['measure']
                        quantity_value = (ingredient['quantity']) * person_count
                        if ingredient_name in ingredients_dict.keys():
                            quantity_value += list(ingredients_dict[ingredient_name].values())[1]
                        measurements_dict = dict(measure = measure_value, quantity = quantity_value)
                        ingredients_dict[ingredient_name] = measurements_dict
    return ingredients_dict

cook_book_dict(file_name)
shopping_list = get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)
pprint(shopping_list)

