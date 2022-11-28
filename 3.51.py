def soft():
    n = 0
    m = 0
    try:
        n = int(input('Введите количество списков: '))
        m = int(input('Введите количество элементов в каждом списке >= 2: '))
    except(ValueError, TypeError):
        print("Введено не целое число")
        soft()

    list_of_lists = []
    minimums = []

    if m >= 2:
        for i in range(n):
            sub_list = []
            for j in range(m):
                try:
                    sub_list.append(int(input('Введите ' + str(j + 1) + ' элемент ' + str(i + 1) + '-того списка: ')))
                except (ValueError, TypeError):
                    print("Введено не целое число")
                    soft()
            list_of_lists.append(sub_list)
            minimums.append(min(sub_list))

    else:
        print('m не больше 2')
        soft()

    maximum = max(minimums)

    print("Максимум: " + str(maximum))


while True:
    soft()
