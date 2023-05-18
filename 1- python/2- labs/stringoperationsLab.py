text = input("Please enter your text: ")
print("------------------------------")
print("please choose the desired operation")
print("1)title() , 2)isnumeric() , 3)zfill()")
while True:
    choice = input("choice is : ")
    # for choice in ('1', '2', '3'):
    if choice == '1':
        print('''
The title() method returns a string where the first character in every word is upper case. Like a header, or a title.

If the word contains a number or a symbol, the first letter after that will be converted to upper case
        ''')
        print("------------------------------")
        print(text.title())
        break
    if choice == '2':
        print('''
The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False
        ''')
        print("------------------------------")
        print(text.isnumeric())
        break
    if choice == '3':
        print('''
The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

If the value of the len parameter is less than the length of the string, no filling is done '''
        )
        print(text.zfill(10))
        break
    else:
        print("Wrong entry!!")
        break

