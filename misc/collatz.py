def collatz(num):
    if (num % 2 == 0):
        return num / 2
    else:
        return 3 * num + 1

print('Enter number')

while(True):
    try:
        input_num = int(input())
        break
    except ValueError:
        print('Input must be an integer')

final_num = input_num
while final_num != 1:
    final_num = int(collatz(final_num))
    print(final_num)
