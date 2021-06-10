import sys

while True:
    print("Type exit to exit.")
    my_input = input()
    if my_input != 'exit':
        print("You entered:", my_input)
    else:
        sys.exit()
