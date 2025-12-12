import random

print('Welcome to my number guessing game')


def guess_game():
    secret_num = random.randint(1,100)
    attempts = 10
    while True:
        print('Attempts left:',attempts)
        user_input = int(input('Can you guess the secret number between 1-100:'))
        if user_input > 100 or user_input < 1:
            print('Only between 1-100')
            continue
        if user_input > secret_num:
            print('Too high! Try Again')
        elif user_input < secret_num:
            print('Too Low! Try Again')
        else:
            print('YOU WIN!',secret_num,'IS THE CORRECT NUMBER')
            break
        attempts -= 1
        if attempts == 0:
            print('Unlucky! You\'ve used all your attempts. Thanks for playing!')
            break
        
guess_game()