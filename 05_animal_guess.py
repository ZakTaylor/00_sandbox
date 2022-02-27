
print("Pick either Ostrich, Lion or Whale")
print("I will attempt to guess your choice")

answer = input("Does the animal live in the water? Y/N ").lower()

if answer == "n":
    answer = input("Does the animal have wings? Y/N ").lower()

    if answer == "y":
        print("It must be an Ostrich!")
    else:
        print("It must be a lion!")
else:
    print("It must be a Whale!")
