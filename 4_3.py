data = {}
for i in range(0, int(input('Введите N:'))+1):
    data[i] = {
        'name': input('Введите имя:'),
        'email': input('Введите email:')
        }
print(data)