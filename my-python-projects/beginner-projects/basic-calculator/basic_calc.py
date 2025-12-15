print('Welcome to my calculator!\n')
def calc():
    first_number = int(input('Enter your first number:'))
    second_number = int(input('Enter your second number:'))
    operation = input('Enter your operation:')

    if operation == '+':
        print(first_number + second_number)
    elif operation == '-':
        print(first_number - second_number)
    elif operation == '*':
        print(first_number * second_number)
    elif operation == '/':
        print(first_number / second_number)
    else:
        print('Invalid Entry')
        
    

while True:
    calc()
    retry_exit = input('Do you want to try again? y/n:')
    if retry_exit == 'y':
        continue    
    elif retry_exit == 'n':
        print('Bye')
        break
    else:
        print('Please select y or n')