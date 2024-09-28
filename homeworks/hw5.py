number = int(input("Введите число от 1 до 4: "))

if number == 1:
    item = "чашка"
elif number == 2:
    item = "тарелка"
elif number == 3:
    item = "кружка"
elif number == 4:
    item = "недействительно"  
else:
    item = "Некорректный ввод. Пожалуйста, введите число от 1 до 4."

if number <= 3:
    print(f"Вы выбрали: {item}")
else:
    print(item)