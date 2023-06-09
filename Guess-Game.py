import random
number = random.randint(1, 100)
player_name = input('Hello, What is your name? \n')
number_of_guesses = 0
print ("okay!" + player_name+ ", i am Guessing a number between 1 and 10...")

while number_of_guesses < 50:
    guess = int(input('What is the number?\n'))
    number_of_guesses += 1
    if guess < number:
        print('Your Guess is too Low')
    if guess > number:
        print('Your Guess is too High')
    if guess == number:
        break

if guess == number:
    print('You Guessed the Number in' + str(number_of_guesses) + 'tries!')
else:
    print('You did not guess the Correct Number,\n The number is ' + str(number))