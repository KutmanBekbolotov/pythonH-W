number = int(input("Enter the number: "))

months = {
    1: "January",
    2: "Febuary",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

if 1 <= number <= 12:
    print(f"Month: {months[number]}")
else:
    print("Undefined try again")

