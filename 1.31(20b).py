import sys

while True:
    a = 0
    b = 0
    E = 0
    k = 0
    formula = 0.0

    try:
        a = int(input("Введите первое число: \nЕсли хотите выйти введите: '1'"))
        if a == 1:
            sys.exit()
        b = int(input("Введите второе число:"))
        E = int(input("Введите E:"))

    except (ValueError, TypeError):
        print("Введено не целое число")

    if (a - b >= E) or (b - a >= E):
        if a > b:
            array = list(range(b, a + 1))
            for i in range(1, E + 1):
                k = array[i]
                formula = 3 / (2 * k ** 2 + 5)
                print(i, 'член ряда равен:', round(formula, 5))
                i += 1

        else:
            array = list(range(a, b + 1))
            for i in range(1, E + 1):
                k = array[i]
                formula = 3 / (2 * k ** 2 + 5)
                print(i, 'член ряда равен:', round(formula, 5))
                i += 1

    else:
        print("Слишком большое число E для данного ряда")




