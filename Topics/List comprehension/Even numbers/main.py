# the following line reads the list from the input; do not modify it, please
my_numbers = [int(x) for x in input().split(" ")]

# work with the variable 'my_numbers'
# my_numbers = [1, 2, 3, 4, 5]
print([x for x in my_numbers if x % 2 == 0])