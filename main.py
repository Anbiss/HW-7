with open('files\cookbook.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        cook_name = line.strip()
        dish_count = int(file.readline())
        ingridients = []
        for _ in range(dish_count):
            ingr_list = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = ingr_list
            ingridients.append({'ingredient_name': ingredient_name,
                                'quantity': int(quantity),
                                'measure': measure})

        file.readline()
        dish = {
            'cook_book': cook_name,
                # 'dish_count': dish_count,
                'ingridients': ingridients}
        cook_book[cook_name] = ingridients

print(cook_book.keys())
print()

#Задание 2

# def get_shop_list_by_dishes(dishes, person_count):
#     res = {}
#     # t = cook_book.keys()
#     # print(t)
#     for ingrid in cook_book:
#         if ingrid == dishes:
#             x = ingrid['ingredient_name']
#             m = ingrid['quantity'] * person_count
#             d = ingrid['measure']
#             s = {'measure' : d, 'quantity' : m}
#             res = {x : s}
#             print(res)
#         print(ingrid)
#     print(cook_book)



def get_shop_list_by_dishes(dishes,person_count):
    res = {}
    t = -1
    while t < 5:
        t += 1
        for ingrid in cook_book[dishes[t]]:
            x = ingrid['ingredient_name']
            m = ingrid['quantity'] * person_count
            d = ingrid['measure']
            s = {'measure': d, 'quantity': m}
            res[x] = s
        # if t != dishes:
        #     break
        print(res)

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
# # print(get_shop_list_by_dishes('Омлет', 2))

