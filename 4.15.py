array = ('Вася', 'Володя', 'Ира', 'Лида', 'Марина')
to_pac = (
    ['Володя', 'Ира', 'Вася'],
    ['Лида', 'Ира', 'Вася'],
    ['Ира', 'Вася'],
    ['Марина', 'Ира', 'Вася'],
    ['Вася', 'Ира', 'Марина'],
    ['Ира', 'Марина'],
    ['Лида', 'Марина'],
    ['Володя', 'Марина']
)
count = 0
good = set()
for i in range(len(array)):
    for j in range(len(to_pac)):
        for k in range(len(to_pac[j])):
            if array[i] == to_pac[j][k]:
                count += 1
                if count == len(array) - 1:
                    good.add(array[i])
    count = 0

print(good)
