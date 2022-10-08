import sys


def integer():
    length = 0
    a = 0
    try:
        length = int(input("Введите размер списка, если хотите выйти введите '0':"))
        if length == 0:
            sys.exit()
    except (ValueError, TypeError):
        print("Задано не целое число")
    positives = 0
    negatives = 0
    for i in range(length):
        try:
            a = int(input(f'Введите {i + 1} целое число:'))
        except (ValueError, TypeError):
            print("Задано не целое число")
            integer()
        if a > 0:
            positives += 1
        if a < 0:
            negatives += 1
    print(f'Вы ввели {positives} положительных чисел и {negatives} отрицательных')


while True:
    integer()
