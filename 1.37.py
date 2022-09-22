import sys

while True:
    N = 0

    try:
        N = int(input('Введите число N < 100: \nЕсли хотите выйти нажмите: "1"'))

    except (ValueError, TypeError):
        print("Введено не целое число")

    if N == 1:
        sys.exit()

    k = 0
    if N < 100:
        if N % 10 == 0:
            while N != 0:
                N -= 10
                k += 1
            else:
                print(k)
        if N % 10 != 0:
            while N > 10:
                N -= 10
                k += 1
            if N % 5 == 0:
                while N != 0:
                    N -= 5
                    k += 1
                else:
                    print(k)
        if N % 10 != 0:
            while N > 10:
                N -= 10
                k += 1
            if N % 5 != 0:
                while N > 5:
                    N -= 5
                    k += 1
            if N % 2 == 0:
                while N != 0:
                    N -= 2
                    k += 1
                else:
                    print(k)
            else:
                N -= 1
                k += 1
                print(k)
    else:
        print("Число N не < 100")