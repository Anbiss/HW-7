# with open('files/cookbook.txt', 'rt', encoding='utf-8') as file:
#     cook_book = {}
#     for line in file:
#         cook_name = line.strip()
#         dish_count = int(file.readline())
#         ingridients = []
#         for _ in range(dish_count):
#             ingr_list = file.readline().strip().split(' | ')
#             ingredient_name, quantity, measure = ingr_list
#             ingridients.append({'ingredient_name': ingredient_name,
#                                 'quantity': int(quantity),
#                                 'measure': measure})
#
#         file.readline()
#         dish = {
#             'cook_book': cook_name,
#                 'dish_count': dish_count,
#                 'ingridients': ingridients}
#         cook_book[cook_name] = ingridients
#
# print(cook_book.keys())
# print()

#Задание 2

#
# def get_shop_list_by_dishes(dishes, person_count):
#     res = {}
#     for i in dishes:
#         for a in cook_book[i]:
#             x = a['ingredient_name']
#             m = a['quantity'] * person_count
#             d = a['measure']
#             if x not in res.keys():
#                 res[x] = {'measure': d, 'quantity': m}
#             elif x in res.keys():
#                 res[x] = {'measure': d, 'quantity': m + m}
#
#     return (res)
#
#
# print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

#Задание 3

# with open('files/1.txt', 'rt', encoding='utf-8') as file:
#     number_str = file.readlines()
#     print(len(number_str))
#     for text in file:
#         print(text.strip())
#
import os

current = os.getcwd()
folder_name = 'files'
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
file_name_4 = '4.txt'

full_patch_1 = os.path.join(current, folder_name, file_name_1)
full_patch_2 = os.path.join(current, folder_name, file_name_2)
full_patch_3 = os.path.join(current, folder_name, file_name_3)
full_patch_4 = os.path.join(current, folder_name, file_name_4)


#текстовый документ №1
with open(full_patch_1, 'rt', encoding='utf-8') as file:
    name_file_1 = '1.txt'
    # print(name_file_1)
    number_str_1 = file.readlines()
    # print(len(number_str_1))
    file.seek(0)
    text_1 = file.read()
    # print(text_1)
    # file.seek(0)
    full_1 = name_file_1, len(number_str_1), text_1
    # print (type(full_1))
    print()


#текстовый документ №2
with open(full_patch_2, 'rt', encoding='utf-8') as file:
    name_file_2 = '2.txt'
    # print(name_file_2)
    number_str_2 = file.readlines()
    # print(len(number_str_2))
    file.seek(0)
    text_2 = file.read()
    # print(text_2)
    full_2 = name_file_2, len(number_str_2), text_2
    # print(full_2)
    print()


#текстовый документ №3
with open(full_patch_3, 'rt', encoding='utf-8') as file:
    name_file_3 = '3.txt'
    # print(name_file_3)
    number_str_3 = file.readlines()
    # print(len(number_str_3))
    file.seek(0)
    text_3 = file.read()
    full_3 = name_file_3, len(number_str_3), (text_3)
    # print(full_3)
    # print(text_3)


#сравнение данных в файлах


comparison = (full_1, full_2, full_3)
comparison = sorted(comparison, key=lambda file: file[1])


with open(full_patch_4, 'w', encoding='utf-8') as file:
    for a in comparison:
        file.write(str(a[0]) + '\n')
        file.write(str(a[1]) + '\n')
        file.write(str(a[2]) + '\n')
