def print_square(a, b):

    start = min(a, b)
    end = max(a, b)

    for num in range(start, end + 1):
        print(f"{num}^2 = {num ** 2}")

a = int(input("enter first number: "))
b = int(input("enter second number: "))

print_square(a, b)