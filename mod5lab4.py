''' cipher lab'''

msg=input("enter a message to encrypt:")

# assert int(shift)
# assert False, "please enter a valid shift value"
while True:
    try:
        shift=int(input("enter a shift value from 1 to 25:"))
        if shift in range(1,26):
            break
        else:
            print("out of range, try again")     
    except ValueError: #make sure user enters Integer not float not letter
        print("this is not an integer number, try again")

     
cipher = ''

for char in msg:
    # is it a letter?
    if char.isalpha():
        # shift its code
        code = ord(char) + shift
        # find the code of the first letter (upper- or lower-case)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # make correction ????????????????
        code -= first
        code %= 26
        # append encoded character to message
        cipher += chr(first + code)
    else:
        # append original character to message
        cipher += char

print(cipher)