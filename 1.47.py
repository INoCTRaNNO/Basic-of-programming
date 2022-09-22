import sys

while True:
    N = 0
    S = 0

    try:
        S = int(input("Введите первое число: \nЕсли хотите выйти введите: '1'"))
        if S == 1:
            sys.exit()
        N = int(input("Введите второе число:"))

    except (ValueError, TypeError):
        print("Введено не целое число")

    resultS = []
    while S > 0:
        resultS.append(S % 10)
        S //= 10

    resultS.reverse()

    resultN = []
    while N > 0:
        resultN.append(N % 10)
        N //= 10

    resultN.reverse()

    result = list(set(resultS) & set(resultN))
    try:
        print("Ответ: %d" % int(''.join(map(str, result))))
    except ValueError:
        print("")
