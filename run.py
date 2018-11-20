from rsa.my_rsa import RSA

rsa = RSA()
rsa.create_keys()

print('--------------------------------------------')
print('----- Example of RSA Encrypt / Decrypt -----')
print('--------------------------------------------\n')

control = True
while control:
    print('( 1 ) Encrypt --- ( 2 ) Decrypt --- ( 3 ) - Exit')
    choice = int(input('Choose an option: '))

    if choice == 1:
        rsa.encrypt()
    elif choice == 2:
        rsa.decrypt()
    elif choice == 3:
        control = False
    else:
        print('Not a valid option')
