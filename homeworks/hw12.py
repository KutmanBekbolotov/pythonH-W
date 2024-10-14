num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

numbers_in_range = []

if 1 <= num1 <= 3:
    numbers_in_range.append(num1)
if 1 <= num2 <= 3:
    numbers_in_range.append(num2)
if 1 <= num3 <= 3:
    numbers_in_range.append(num3)

if numbers_in_range:
    print(f"Числа, которые принадлежат интервалу [1, 3]: {numbers_in_range}")
else:
    print("Нет чисел, принадлежащих интервалу [1, 3].")