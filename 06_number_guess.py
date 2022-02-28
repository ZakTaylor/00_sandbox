
guess_left = 3
number = 9

while guess_left > 0:
    try:
        guess_number = int(input("Guess a number between 1 and 10! "))
        guess_left -= 1

        if guess_number == number:
            print("Correct, {} was the number! ".format(number))
            break
        else:
            print("Incorrect, you have {} guesses left! ".format(guess_left))
    except ValueError:
        print("Please put in a whole number! ")
