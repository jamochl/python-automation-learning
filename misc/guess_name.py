familyNames = ["Bob", "Dillan", "Cherry", "Jenny", "Macey"]

while True:
    # prompt user to guess a name in the family
    print("Guess a name in the family!")
    # check name
    userInput = input()
    if userInput in familyNames:
        break
    # break or continue
    print("Incorrect!")

print(f"Yes, {userInput} is in the family!")
