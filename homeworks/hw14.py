base = float(input("Введите число, которое нужно возводить в степень: "))
limit = int(input("Введите предел для степени: "))

for exponent in range(1, limit + 1):
    result = base ** exponent
    print(f"{base} ^ {exponent} = {result}")