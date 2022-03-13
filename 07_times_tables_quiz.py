# Welcome
print("---Welcome to the Times Table Quiz---")
print()
answer = 0

# Ask for times table requirements
times_table = int(input("Enter a times table that you would like to be tested on! "))
print()

max_value = int(input("Enter the maximum value for your times table! "))
print()

# Quiz questions
print("---You will now be tested on the {} times table---".format(times_table))
print()

for x in range(1,max_value):
    try:
        answer = x * times_table
        user_answer = int(input("{} times {} is ...? ".format(x,times_table,)))
        if user_answer == answer:
            print("Correct")
        else:
            print("Incorrect")
    except ValueError:
        print("Please enter a whole number")

print()
# End quiz
print("---Thanks for taking the quiz---")
