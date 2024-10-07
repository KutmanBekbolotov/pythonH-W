number = int(input("Enter the number 1-4: "))

seasons = {
    1: "Winter",
    2: "Spring",
    3: "Summer",
    4: "Fall"
}

if number in seasons:
    print(seasons[number])
else:
    print("Error")