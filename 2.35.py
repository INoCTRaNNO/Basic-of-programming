import sys

while True:
    s = max(str(input("Введите строку, если хотите выйти введите: `1`")).split(" ")).replace("a", "b")
    if s == "1":
        sys.exit()
    print(s)

