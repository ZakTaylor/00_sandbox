
total_cost = 0.00
# Welcome to the restaurant. Menu yes/no
print("---Welcome to Mike's Pizza Restaurant---")
print()

print("We bake quality Pizza for our Customers! ")
print()

view_menu = input("Would you like to view the Menu? ").lower()
print()

if view_menu == "yes" or "y":
    print("---Menu---")
    print()
    print("Base options:")
    print()
    print("Thick crust     $8.00")
    print("Thin crust      $10.00")
    print()
    print("Size options: ")
    print()
    print("8 inch          No additional charge")
    print("10 inch         No additional charge")
    print("12 inch         $2 additional charge")
    print("14 inch         $2 additional charge")
    print("18 inch         $2 additional charge")
    print()
    print("Cheese: ")
    print()
    print("Cheese          Included")
    print("No cheese       $0.50 Discount")
    print()
    print("Type of Pizza")
    print()
    print("Margarita       $0")
    print("Vegetable       $1")
    print("Vegan           $2")
    print("Hawaiian        $2")
    print("Meat feast      $2")
elif view_menu == "no" or "n":
    print("---Now how would you like your Pizza made today?---")
else:
    view_menu = input("Please answer Yes or No! ")

print()

# Making of the Pizza
base_pizza = input("Would you like Thick or Thin crust for your Pizza? ").lower()

if base_pizza == "thick":
    total_cost = total_cost + 8.00
elif base_pizza == "thin":
    total_cost = total_cost + 10.00
else:
    print()
    base_pizza = input("Please choose from the available Pizza crusts! ").lower()

print()
size_pizza = input("Would you like an 8, 10, 12, 14 or 18 inch Pizza base? ")

if size_pizza == "8" or "10":
    total_cost = total_cost
elif size_pizza == "12" or "14" or "18":
    total_cost = total_cost + 2.00
else:
    print()
    size_pizza = input("Please choose from the available Pizza sizes! ").lower()

print()
cheese_pizza = input("Would you like cheese on your Pizza? ").lower()

if cheese_pizza == "yes" or "y":
    total_cost = total_cost
elif cheese_pizza == "no" or "n":
    total_cost = total_cost - 0.50
else:
    print()
    cheese_pizza = input("Please choose Yes or No for cheese! ").lower()

print()
type_pizza = input("What type of Pizza would you like today? ").lower()

if type_pizza == "margarita":
    total_cost = total_cost
elif type_pizza == "vegetable":
    total_cost = total_cost + 1.00
elif type_pizza == "vegan" or "hawaiian" or "meat feast":
    total_cost = total_cost + 2.00
else:
    print()
    type_pizza = input("Please choose from the available Pizza types! ").lower()

print()

# Voucher
voucher_code = input("Do you have a Voucher you would like to redeem? ").lower()

if voucher_code == "yes" or "y":
    voucher_code = input("Please enter your Voucher code: ")
    if voucher_code == "funfriday":
        total_cost = total_cost - 2.00
    else:
        voucher_code = input("Please enter an existing code! ").lower()
elif voucher_code == "no" or "n":
    total_cost = total_cost
else:
    voucher_code = input("Please choose Yes or No for Voucher code! ").lower()

print()
# Checking the order
order_correct = input("So today you would like a {} inch, {} Pizza with {} crust and {} to cheese? ".format(size_pizza, type_pizza, base_pizza, cheese_pizza))

if order_correct == "yes" or "no":
    print("Then your total today comes to ${} ".format(total_cost))
    print("Your Pizza will be made in 15 minutes! ")
    print()
    print("---Thank you for ordering a Pizza from Mike's Pizza Restaurant---")
elif order_correct == "no" or "n":
    print("Sorry for the inconvenience. Please re-fresh the page and re-order! ")
else:
    order_correct = input("Please choose Yes or No so we can make your order! ")
