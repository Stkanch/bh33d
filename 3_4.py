numbers = input('Введите 3 числа : ')
input('Положительное = True, Отрицательное = False. Для продолжения нажмите enter!')
number1 = (numbers.split()[0])
number2 = (numbers.split()[1])
number3 = (numbers.split()[2])
print(number1.isdigit(), number2.isdigit(), number3.isdigit())
print(3 - (number1 + number2 + number3).count("-"), 'положительных')
print(3 - (3 - (number1 + number2 + number3).count("-")), 'отрицательных')



