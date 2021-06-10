passwordFile = open('secret_pass.txt')
secretPassword = passwordFile.readline().strip()
print('Secret pass is:', secretPassword)
print('Enter your password')
typedPassword = input()

if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '12345':
        print('That password is one that an unsmart dude puts on their luggage')
else:
    print('Access denied')

