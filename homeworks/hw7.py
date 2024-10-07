def sum_of_digits(n):
    sum_digits = 0

    for digit in str(n):

        sum_digits += int(digit)
    return sum_digits

n = int(input("Enter number: "))

print(f"Sum of number {n} equals {sum_of_digits(n)}")