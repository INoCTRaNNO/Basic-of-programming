import sys


def move_Right():
    lst = [1, 2, 3, 4, 5, 6]
    n = int(input("Введите целое число, если хотите выйти введите '-1':"))
    if n == -1:
        sys.exit()
    if n > len(lst):
        while n > len(lst):
            n -= len(lst)
        lst = lst[-n:] + lst[:-n]
    else:
        lst = lst[-n:] + lst[:-n]

    print(lst)


while True:
    move_Right()
