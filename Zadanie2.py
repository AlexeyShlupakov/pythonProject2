# Задание 1
spisok = [-1, 2.5, 6, 'text', None]
print(spisok)


def my_type(el):
    for el in range(len(spisok)):
        print(type(spisok[el]))
    return


my_type(spisok)

# Задание 2
a = list(input("Введите элементы списка: "))
a[::2], a[1::2] = a[1::2], a[::2]
print(a)

# Задание 3
period_list = ['Зима', 'Весна', 'Лето', 'Осень']
period_dict = {1: 'Зимний_период', 2: 'Весенний_период', 3: 'Летний_период', 4: 'Осенний_период'}
month = int(input("Введите номер месяца "))
if month == 1 or month == 12 or month == 2:
    print(period_dict.get(1))
    print(period_list[0])
elif month == 3 or month == 4 or month == 5:
    print(period_dict.get(2))
    print(period_list[1])
elif month == 6 or month == 7 or month == 8:
    print(period_dict.get(3))
    print(period_list[2])

elif month == 9 or month == 10 or month == 11:
    print(period_dict.get(4))
    print(period_list[3])
else:
    print("Даже дети знают, что всего двенадцать месяцев!")

# Задание 4
stroka = input("введите строку ")
word = []
schetchik = 1
for el in range(stroka.count(' ') + 1):
    word = stroka.split()
    if len(str(word)) <= 10:
        print(f" {schetchik} {word[el]}")
        schetchik += 1
    else:
        print(f" {schetchik} {word[el][0:10]}")
        schetchik += 1

# Задание 5
my_list = [7, 5, 3, 3, 2]
print(my_list)
new_element = int(input("Введите число: "))
while new_element != 999999999999999999999999999999999999999:
    for el in range(len(my_list)):
        if my_list[el] == new_element:
            my_list.insert(el + 1, new_element)
            break
        elif my_list[0] < new_element:
            my_list.insert(0, new_element)
        elif my_list[-1] > new_element:
            my_list.append(new_element)
        elif my_list[el] > new_element and my_list[el + 1] < new_element:
            my_list.insert(el + 1, new_element)
    print(f"текущий список - {my_list}")
    new_element = int(input("Введите число "))

# Задание 6
goods = []
features = {'Название товара': '', 'Цена товара': '', 'Количество товара': '', 'Единица измерения': ''}
analytics = {'Название товара': [], 'Цена товара': [], 'Количество товара': [], 'Единица измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input(
        "Для ввода товара нажмите 'Enter', Для вывода аналитики по товарам введите 'A', Для выхода введите 'Q'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
    for f in features.keys():
        feature_ = input(f'Введите "{f}"')
        features[f] = int(feature_) if (f == 'Цена товара' or f == 'Количество товара') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))