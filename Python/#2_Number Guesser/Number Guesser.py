import random


def dom_rang():

    global lower_limit
    global upper_limit

    print('')

    lower_limit = input('Please input the lower limit of your guess:')
    upper_limit = input('Please input the upper limit of your guess:')

    if lower_limit.isdigit() and upper_limit.isdigit():

        if int(upper_limit) > int(lower_limit):

            pass

        else:

            print('')

            print('Upper limit should be greator than the lower limit.')

            dom_rang()

    else:

        print('')

        print('Please type a number.')

        dom_rang()


def guess():

    global user_guess

    user_guess = input('Please input your guess:')

    if user_guess.isdigit():

        pass

        if int(user_guess) >= int(lower_limit) and int(user_guess) <= int(upper_limit):

            pass

        else:

            print('Guess should be within the domain and range.')

            guess()

    else:

        print('It should be a digit.')

        guess()


def random_generator():

    global random_number

    random_number = random.randrange(int(lower_limit), int(upper_limit))


dom_rang()
guess()
random_generator()


def while_loop():

    guess_count = 1

    while int(user_guess) != int(random_number):

        if int(random_number) < int(user_guess):

            print('A little lower!')

        else:

            print('Higher, Higher!')

        guess_count += 1

        guess()

    else:

        print('Yay!!! Correct Guess.\n\n')

        print('Summary'.center(20, '='))

        print(

            f' Your guess = {user_guess}\n',

            f'Computer choice = {random_number}\n',

            f'No. of Tries = {guess_count}\n'

        )


while_loop()
