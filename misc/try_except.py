def divide(num):
    try:
        return 42 / num
    except ZeroDivisionError:
        print('Error: Invalid argument')


print(divide(2))
print(divide(12))
print(divide(0))
print(divide(1))
