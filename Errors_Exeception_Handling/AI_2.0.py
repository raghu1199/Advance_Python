def interact():
    while True:  # keep looping until user reach break statement
        user_input = input('Please input an integer:')     # turn the user input into an integer
        try:
            num=int(user_input)
        except ValueError:
            print("Please input integers only.")
        else:
            print('{} is {}.'.format(num, 'even' if num % 2 == 0 else 'odd'))     # print out the message '{user_input} is {even/odd}.'
        user_input = input('Do you want to play again? (y/N):')
        if user_input != 'y':   # quit if the user didn't input `y`
            print('Goodbye.')
            break   # break the while loop to quit

interact()