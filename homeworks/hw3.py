month = int(input("Enter the number of month: "))

if month == 1 or month == 2 or month ==12:
    season = "Winter"
elif month >= 3 and month <=5:
    season = "Spring"
elif month >= 6 and month <= 8:
    season = "Summer"
elif month >= 9 and month <= 11:
    seson = "Fall"

else:
    seson = "No seson found"

print(f"Season: {season}")