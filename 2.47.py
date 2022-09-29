import sys

while True:
    try:
        N1 = int(input("Введите целое число, если хотите выйти введите: `1`:"))
        if N1 == 1:
            sys.exit()
        N2 = int(input("Введите целое число:"))
        S1 = str(input("Введите строку:"))
        S2 = str(input("Введите строку:"))
    except (ValueError, TypeError):
        print("Не верно заданы значения")

    s = len(S2) - N2
    S = S1[0: N1] + S2[s:]
    print(S)

