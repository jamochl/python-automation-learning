catNames = []
while True:
    print(f"Enter the name of Cat {str(len(catNames) + 1)} here (or enter nothing to stop)")
    userInput = input()
    if userInput == '':
        break
    catNames = catNames + [userInput]
print('The cat names are:')
for name in catNames:
    print(' ' + name)
