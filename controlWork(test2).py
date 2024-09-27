number = int(input("Enter th number: "))

numbers_to_word = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

if 1 <= number <=5:
    print(f"Number {number} in words: {numbers_to_word[number]}")
else:
    print("Undefined")