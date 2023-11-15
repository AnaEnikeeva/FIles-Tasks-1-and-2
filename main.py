with open('recipes.txt', encoding = 'utf-8') as recipes_file:
    cook_book = {}
    for string in recipes_file:
        dish = string.strip()
        ingredients_count = int(recipes_file.readline().strip())
        dish_dict = []
        for item in range(ingredients_count):
            ingredients_name, quantity, measure = recipes_file.readline().strip().split('|')
            dish_dict.append({'ingredient_name': ingredients_name,
                              'quantity': quantity,
                              'measure': measure})
        cook_book[dish] = dish_dict
        recipes_file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    ingredient_dict = {}
    for _dish in dishes:
        for ingredient in cook_book[_dish]:
            ingredients_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * person_count,
                                      'measure': ingredient['measure']})])
            if ingredient_dict.get(ingredient['ingredient_name']) == 'None':
                union = (int(ingredient_dict[ingredient['ingredient_name']]['quantity']) + 
                         int(ingredients_list[ingredient['ingredient_name']]['quantity']))
                ingredient_dict[ingredient['ingredient_name']]['quantity'] = union
            else:
                ingredient_dict.update(ingredients_list)
    return ingredient_dict

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос', 'Утка по-пекински'], 3))