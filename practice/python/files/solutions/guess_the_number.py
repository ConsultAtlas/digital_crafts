print('I am thinking of a number between 1 and 10.')
user_guess = int(raw_input('What is the number?'))
secret_number = 4

#contdition is that the user guess is either correct or incorrect
while user_guess != secret_number:
    print('Try again. :)')
    #if the user guess is incorrect, it only has two possible options: high or low.
    if user_guess > secret_number:
        print('That is too high!')
        user_guess = int(raw_input('What is the number?'))
    else:
        print('That is too low!')
        user_guess = int(raw_input('What is the number?'))

print('Correct!')



    #if user_guess == secret_number:
    #    print ('Great job!')
    #    break
