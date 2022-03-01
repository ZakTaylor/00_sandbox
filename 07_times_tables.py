times_table = int(input("What number times table would you like to see? "))
answer = 0

print("Here is the {} times table".format(times_table))
for x in range(1,13):
    answer = x * times_table
    print("{} times {} is {}".format(x,times_table,answer))
