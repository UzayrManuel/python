to_do_list = ["Make breakfast","Walk my dog"]


def add_to_list():
    add_item = input('Add Item:')
    to_do_list.append(add_item)
    print('You\'ve successfully added an item')
    input('Click any button to continue')
    
def remove_from_list():
    if not to_do_list:
        print('There are no items to remove')
        input('Click any button to continue')
    else:
        remove_item = int(input('Remove Item:'))
        to_do_list.pop(remove_item - 1)
        print('You\'ve successfully removed an item')
        input('Click any button to continue')
    
def check_list():
    for index, x in enumerate(to_do_list, start = 1):
        print(index, x)
    input('Click any button to continue')


while True:
    print('To-Do List Tool\n')
    print('Type number:')
    print('1. Add Item\n2. Remove Item\n3. Check List\n4. Exit')
    user_input = int(input('Choose option:'))
    if user_input == 1:
        add_to_list()       
    elif user_input == 2:
        remove_from_list()
    elif user_input == 3:
        check_list()
    elif user_input == 4:
        break
    else:
        print('Choose a valid option')