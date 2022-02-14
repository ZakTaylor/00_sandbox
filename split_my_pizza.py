print("Welcome to split my pizza")
print("Each slice of pizza is 0.50$")

print()


pizza = int(input("How many slices of pizza would you like?"))
people = int(input("How many people are sharing?"))



each = pizza // people
left = pizza % people
bill = pizza * 0.50

print()

print("Slices each!")
print(each)
print("Slices left")
print(left)

print()

print("Your total amount of money has come to {}$ for {} slices of pizza! ".format(bill, pizza))
