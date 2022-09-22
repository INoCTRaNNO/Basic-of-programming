import sys

while True:
    a = 0
    b = 0
    n = 0
    k = 0
    formula = 0.0
    summa = 0.0

    try:
        a = int(input("Введите первое число: \nЕсли хотите выйти введите: '1'"))
        if a == 1:
            sys.exit()
        b = int(input("Введите второе число:"))
        n = int(input("Введите n:"))

    except (ValueError, TypeError):
        print("Введено не целое число")

    if (a - b >= n) or (b - a >= n):
        if a > b:
            array = list(range(b, a + 1))
            for i in range(1, n + 1):
                k = array[i]
                formula = 3 / (2 * k ** 2 + 5)
                i += 1
                summa += formula
        else:
            array = list(range(a, b + 1))
            for i in range(1, n + 1):
                k = array[i]
                formula = 3 / (2 * k ** 2 + 5)
                i += 1
                summa += formula
    else:
        print("Слишком большое число n для данного ряда")
    print(round(summa, 5))
