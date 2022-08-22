numbers = input('Введите 3 числа : ')
number1 = int(numbers.split()[0])
number2 = int(numbers.split()[1])
number3 = int(numbers.split()[2])
otvet = (number3 + number2 + number1) / 3
print(round(otvet, 3))