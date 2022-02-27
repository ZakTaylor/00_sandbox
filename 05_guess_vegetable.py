
print("Pick either Broccoli, Peas, Sweetcorn or Carrot! ")
print("I will attempt to guess the Vegetable you pick! ")
print()
answer = input("Is the Vegetable green Y/N? ").lower()

if answer == "y":
    answer = input("Does the Vegetable look like a Tree. Y/N? ").lower()

    if answer == "y":
        print("It must be Broccoli! ")
    elif answer == "n":
        print("It must be Peas! ")
    else:
        answer = input("Please answer with Y/N! ").lower()

elif answer == "n":
    answer = input("Is the Vegetable Orange. Y/N? ").lower()

    if answer == "y":
        print("It must be Carrot! ")
    elif answer == "n":
        print("It must be Sweetcorn! ")
    else:
        answer = input("Please answer with Y/N! ").lower()

else:
    answer = input("Please answer with Y/N! ").lower()
