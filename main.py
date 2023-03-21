# Alexander Osterude Rey

def encoder(password):
    encoded_pass = ''
    for i in password:
        val = int(i) + 3
        if val >= 10:
            val -= 10
        encoded_pass += str(val)
    return encoded_pass


def decoder(password):
    decoded_pass = ""
    for element in password:
        element = int(element) - 3
        if element == -3:
            element = 7
        if element == -2:
            element = 8
        if element == -1:
            element = 9
        decoded_pass += str(element)

    return decoded_pass

    pass


if __name__ == '__main__':
    while True:
        print('''
Menu
-------------
1. Encode
2. Decode
3. Quit\n''')
        choice = input('Please enter an option: ')

        if choice == '1':
            password = input('Please enter your password to encode: ')
            encoded_pass = encoder(password)
            print('Your password has been encoded and stored!')
        elif choice == '2':
            decoded_pass = decoder(encoded_pass)
            print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}.')
        elif choice == '3':
            break
