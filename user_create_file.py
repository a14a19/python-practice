file_name = input("Please enter file name?(without extension) \n")
userInput = input('Please enter context for file: \n')
with open (f'{file_name}.txt', 'w') as user:
    user.write(f'{userInput}')

userUpdate = None
# creating and updating the file through user input
while userUpdate not in ['y', 'n']:
    userUpdate = input('Do you want to update file with new line?(y or n) \n')
    if userUpdate == 'y':
        userInput2 = input('Please enter new text for file: \n')
        with open(f'{file_name}.txt', 'a') as newLine:
            newLine.write(f'\n{userInput2}')
    else:
        pass

view_file = input("Do you want to view the file?(y or n) \n")
# giving output to user, for the file user created earlier
while view_file not in ['y', 'n']:
    view_file = input("Do you want to view the file?(Please enter y or n) \n")
    if view_file == 'y':
        with open(f'{file_name}.txt', 'r') as file:
            file = file.read()
        print(f'\nYour file contains: \n{file}')
    else:
        pass