letter = input("Введите букву от 'a' до 'е': ")

alphabet = "абвгде"

if letter in alphabet:

    number = alphabet.index(letter) + 1
    print(f"Номер буквы '{letter}' в алфавите: {number}")
else:
    print("Error")