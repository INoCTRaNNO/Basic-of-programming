import sys


def sort_merge(list1, list2):
    return sorted(list1 + list2)


def integer():
    array_first = []
    array_two = []
    array = []
    a = 0
    b = 0
    c = 0
    d = 0
    try:
        a = int(input("Введите размер первого списка, если хотите выйти введите '0':"))
        if a == 0:
            sys.exit()
    except (ValueError, TypeError):
        print("Задано не целое число")
        integer()

    for i in range(a):
        try:
            b = int(input(f'Введите {i + 1} целое число:'))
        except (ValueError, TypeError):
            print("Задано не целое число")
            integer()
        array_first.append(b)
    try:
        c = int(input("Введите размер второго списка:"))
    except (ValueError, TypeError):
        print("Задано не целое число")
        integer()

    for i in range(c):
        try:
            d = int(input(f'Введите {i + 1} целое число:'))
        except (ValueError, TypeError):
            print("Задано не целое число")
            integer()
        array_two.append(d)

    array = sort_merge(array_first, array_two)
    print(array[0: a], array[a:])


while True:
    integer()
