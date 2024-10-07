number = int(input("Enter the number 1-4: "))

actions = {
    1: "stay",
    2: "wait",
    3: "go",
    4: "run"
}

if number in actions:
    print(actions[number])
else:
    print ("error")
