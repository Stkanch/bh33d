n = input('Введите текст:')
count = {}
for i in n:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
print(count)

